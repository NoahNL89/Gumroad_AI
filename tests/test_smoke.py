#!/usr/bin/env python3
"""
Schep Digital — smoke tests. No external test framework required.

    python3 tests/test_smoke.py        # run all, exit non-zero on failure
    pytest tests/test_smoke.py         # also works if pytest is installed

Covers the survivability-critical, unattended-cron paths:
  - product_builder: spec validation, escaping, every block type
  - bot copy: rate-limit logic, no false product claims, all templates render
  - query.py: revenue/survival math (refunds excluded from net)
"""
import importlib.util
import io
import json
import os
import sqlite3
import sys
import tempfile
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
sys.path.insert(0, str(ROOT / "bot"))
sys.path.insert(0, str(ROOT / "db"))


def _load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


# ── product_builder ─────────────────────────────────────────────────────────
import product_builder as pb  # noqa: E402


def test_builder_demo_renders_every_block():
    html = pb.build_html(pb.build_demo_spec())
    for cls in ('class="cover"', "section-header", "prompt-block", "checklist",
                "<table>", "stat-card", 'class="callout amber"'):
        assert cls in html, f"missing {cls}"


def test_builder_escapes_content():
    html = pb.build_html(pb.build_demo_spec())
    assert "&lt;tag&gt;" in html and "<tag>" not in html, "content not escaped"
    assert "&amp; ampersand" in html, "ampersand not escaped"


def test_builder_validates_required_fields():
    errs = pb.validate_spec({"slug": "x"})  # missing title/subtitle/eyebrow/chapters
    assert any("title" in e for e in errs)
    assert any("chapters" in e for e in errs)


def test_builder_rejects_unknown_block_type():
    bad = pb.build_demo_spec()
    bad["chapters"][0]["blocks"].append({"type": "nope"})
    try:
        pb.build_html(bad)
    except ValueError:
        return
    raise AssertionError("unknown block type should raise ValueError")


# ── bots: copy correctness + rate limiting ──────────────────────────────────
def _make_promotions_db(path, mastodon_posts=0, bluesky_posts=0, pinterest_posts=0, pinterest_sandbox_posts=0):
    con = sqlite3.connect(path)
    con.execute("""CREATE TABLE promotions (platform TEXT, product_id TEXT, url TEXT,
                   content TEXT, posted_at TEXT)""")
    now = "datetime('now')"
    for plat, n in (
        ("mastodon", mastodon_posts),
        ("bluesky", bluesky_posts),
        ("pinterest", pinterest_posts),
        ("pinterest_sandbox", pinterest_sandbox_posts),
    ):
        for _ in range(n):
            con.execute(f"INSERT INTO promotions VALUES (?,?,?,?,{now})",
                        (plat, "id", "url", "x"))
    con.commit()
    con.close()


def _seed_pinterest_products_db(path):
    con = sqlite3.connect(path)
    con.execute("""CREATE TABLE products (
                   id TEXT, name TEXT, formatted_price TEXT, short_url TEXT,
                   thumbnail_url TEXT, published INTEGER, price_cents INTEGER)""")
    con.execute("""CREATE TABLE promotions (
                   platform TEXT, product_id TEXT, url TEXT, content TEXT, posted_at TEXT)""")
    con.execute(
        "INSERT INTO products VALUES (?,?,?,?,?,?,?)",
        (
            "prod_1",
            "Pinterest Demo Product",
            "€7.99",
            "https://schephenk.gumroad.com/l/demo",
            "https://example.com/demo.jpg",
            1,
            799,
        ),
    )
    con.commit()
    con.close()


def _seed_catalog_products_db(path):
    con = sqlite3.connect(path)
    con.execute("""CREATE TABLE products (
                   id TEXT, name TEXT, description TEXT, price_cents INTEGER,
                   currency TEXT, formatted_price TEXT, short_url TEXT,
                   thumbnail_url TEXT, published INTEGER)""")
    con.executemany(
        "INSERT INTO products VALUES (?,?,?,?,?,?,?,?,?)",
        [
            (
                "paid_1",
                "AI Prompt Pack",
                "Useful prompts for creators.",
                799,
                "eur",
                "€7.99",
                "https://schephenk.gumroad.com/l/prompts",
                "https://example.com/prompts.jpg",
                1,
            ),
            (
                "sub_1",
                "Monthly Vault",
                "Subscription.",
                99,
                "eur",
                "€0.99 a month",
                "https://schephenk.gumroad.com/l/monthly",
                "https://example.com/monthly.jpg",
                1,
            ),
        ],
    )
    con.commit()
    con.close()


def _bots():
    """Import both bot modules; skip cleanly if their network deps aren't installed."""
    mods = {}
    for name, path in (("mastodon_bot", ROOT / "bot/mastodon_bot.py"),
                       ("bluesky_bot", ROOT / "bot/bluesky_bot.py"),
                       ("pinterest_bot", ROOT / "bot/pinterest_bot.py")):
        try:
            mods[name] = _load(path, name)
        except SystemExit:
            print(f"  (skip {name}: optional dependency not installed)")
    return mods


def test_bot_copy_has_no_false_claims():
    for name, m in _bots().items():
        # generic templates must never imply the product is a set of prompts
        for t in m.GENERIC_VALUE_TEMPLATES:
            assert "prompt" not in t.lower(), f"{name}: generic template mentions prompts"
        # the old hardcoded "75" must be gone everywhere
        for t in m.VALUE_TEMPLATES + m.SELL_TEMPLATES + m.BUNDLE_TEMPLATES:
            assert "75" not in t, f"{name}: stray '75' in template"
        # detection works
        assert m.is_prompt_product("75 Power Prompts for AI Masters")
        assert not m.is_prompt_product("Notion Habit Architecture")


def test_bot_templates_all_format():
    base = dict(name="Test Product", price="€9.99", url="https://x", code="LAUNCH30")
    for name, m in _bots().items():
        extra = {"hashtags": "#x"} if name == "mastodon_bot" else {}
        for t in m.VALUE_TEMPLATES + m.SELL_TEMPLATES + m.BUNDLE_TEMPLATES:
            t.format(**base, **extra)  # raises KeyError on a bad placeholder


def test_bot_rate_limit_blocks_at_three():
    mods = _bots()
    with tempfile.TemporaryDirectory() as d:
        dbp = Path(d) / "store.db"
        _make_promotions_db(str(dbp), mastodon_posts=3, bluesky_posts=0)
        if "mastodon_bot" in mods:
            mods["mastodon_bot"].DB_PATH = dbp
            assert mods["mastodon_bot"].check_rate_limit() is False, "should block at 3 posts"
        if "bluesky_bot" in mods:
            mods["bluesky_bot"].DB_PATH = dbp
            assert mods["bluesky_bot"].check_rate_limit() is True, "should allow at 0 posts"
        if "pinterest_bot" in mods:
            mods["pinterest_bot"].DB_PATH = dbp
            assert mods["pinterest_bot"].check_rate_limit() is True, "should allow at 0 posts"

        dbp.unlink()
        _make_promotions_db(str(dbp), pinterest_sandbox_posts=3)
        if "pinterest_bot" in mods:
            mods["pinterest_bot"].DB_PATH = dbp
            assert mods["pinterest_bot"].check_rate_limit() is False, "should block Pinterest sandbox at 3 posts"


def test_pinterest_draft_requires_manual_approval():
    mods = _bots()
    if "pinterest_bot" not in mods:
        return
    pinterest = mods["pinterest_bot"]
    with tempfile.TemporaryDirectory() as d:
        root = Path(d)
        dbp = root / "store.db"
        drafts = root / "queue"
        _seed_pinterest_products_db(str(dbp))
        pinterest.DB_PATH = dbp
        pinterest.DRAFT_DIR = drafts
        with patch.object(pinterest, "api_request", side_effect=AssertionError("draft must not call Pinterest API")):
            path = pinterest.write_draft("prod_1")
        data = json.loads(path.read_text())
    assert data["status"] == "needs_manual_approval"
    assert data["approval_required"] is True
    assert data["product"]["id"] == "prod_1"
    assert data["pin"]["link"] == "https://schephenk.gumroad.com/l/demo"


def test_pinterest_save_env_values_updates_tokens():
    mods = _bots()
    if "pinterest_bot" not in mods:
        return
    pinterest = mods["pinterest_bot"]
    with tempfile.TemporaryDirectory() as d:
        envp = Path(d) / ".env"
        envp.write_text("PINTEREST_ACCESS_TOKEN=old\nPINTEREST_BOARD_NAME=Board\n")
        old_env_path = pinterest.ENV_PATH
        try:
            pinterest.ENV_PATH = envp
            pinterest.save_env_values({
                "PINTEREST_ACCESS_TOKEN": "new-access",
                "PINTEREST_REFRESH_TOKEN": "new-refresh",
            })
        finally:
            pinterest.ENV_PATH = old_env_path
        text = envp.read_text()
    assert "PINTEREST_ACCESS_TOKEN=new-access" in text
    assert "PINTEREST_REFRESH_TOKEN=new-refresh" in text
    assert "PINTEREST_BOARD_NAME=Board" in text


def test_pinterest_api_base_forces_sandbox_by_default():
    mods = _bots()
    if "pinterest_bot" not in mods:
        return
    pinterest = mods["pinterest_bot"]
    old = {
        "PINTEREST_API_BASE": os.environ.get("PINTEREST_API_BASE"),
        "PINTEREST_SANDBOX_API_BASE": os.environ.get("PINTEREST_SANDBOX_API_BASE"),
        "PINTEREST_ALLOW_PRODUCTION": os.environ.get("PINTEREST_ALLOW_PRODUCTION"),
    }
    try:
        os.environ["PINTEREST_API_BASE"] = "https://api.pinterest.com/v5"
        os.environ["PINTEREST_SANDBOX_API_BASE"] = "https://api-sandbox.pinterest.com/v5"
        os.environ.pop("PINTEREST_ALLOW_PRODUCTION", None)
        assert pinterest.api_base() == "https://api-sandbox.pinterest.com/v5"
        assert pinterest.is_sandbox() is True
    finally:
        for key, value in old.items():
            if value is None:
                os.environ.pop(key, None)
            else:
                os.environ[key] = value


def test_pinterest_catalog_feed_rewrites_claimed_domain_and_skips_subscriptions():
    catalog = _load(ROOT / "scripts/build_pinterest_catalog.py", "pinterest_catalog")
    with tempfile.TemporaryDirectory() as d:
        dbp = Path(d) / "store.db"
        out = Path(d) / "catalog.csv"
        _seed_catalog_products_db(str(dbp))
        rows, skipped = catalog.rows_from_db(dbp, "https://store.schep.dev")
        catalog.write_csv(rows, out)
        text = out.read_text()
    assert len(rows) == 1
    assert rows[0]["link"] == "https://store.schep.dev/l/prompts"
    assert rows[0]["price"] == "7.99 EUR"
    assert rows[0]["availability"] == "in stock"
    assert rows[0]["google_product_category"] == "8022"
    assert "Monthly Vault" in skipped[0][0]
    assert '"id","title","description","link","image_link","price","availability"' in text


def test_pinterest_catalog_uses_specific_google_taxonomy_leaf_ids():
    catalog = _load(ROOT / "scripts/build_pinterest_catalog.py", "pinterest_catalog_categories")
    assert catalog.google_product_category("Instagram Growth Templates") == "8022"
    assert catalog.google_product_category("The Local LLM Guide") == "543542"
    assert catalog.google_product_category("AI Art Asset Collection") == "500046"
    assert catalog.google_product_category("AI-to-Blender Mastery Kit") == "6027"


def test_catalog_server_requires_basic_auth():
    server = _load(ROOT / "scripts/catalog_server.py", "catalog_server_test")
    with tempfile.TemporaryDirectory() as d:
        catalog = Path(d) / "pinterest_catalog.csv"
        catalog.write_text("id,title\n1,Test\n")
        old_path = server.CATALOG_PATH
        old_user = server.USERNAME
        old_password = server.PASSWORD
        try:
            server.CATALOG_PATH = catalog
            server.USERNAME = "user"
            server.PASSWORD = "pass"
            handler = object.__new__(server.Handler)
            handler.headers = {}
            assert handler.authenticated() is False
            import base64
            token = base64.b64encode(b"user:pass").decode()
            handler.headers = {"Authorization": f"Basic {token}"}
            assert handler.authenticated() is True
        finally:
            server.CATALOG_PATH = old_path
            server.USERNAME = old_user
            server.PASSWORD = old_password


# ── query.py: revenue math ──────────────────────────────────────────────────
def _seed_sales_db(path):
    con = sqlite3.connect(path)
    con.execute("""CREATE TABLE sales (product_name TEXT, email TEXT, formatted_price TEXT,
                   price_cents INTEGER, refunded INTEGER, sale_timestamp TEXT)""")
    from datetime import datetime
    month = datetime.now().strftime("%Y-%m")
    rows = [
        ("Prompt Pack", "a@x.com", "€9.99", 999, 0, f"{month}-05T10:00:00"),
        ("Prompt Pack", "b@x.com", "€9.99", 999, 0, f"{month}-06T10:00:00"),
        ("Refunded One", "c@x.com", "€9.99", 999, 1, f"{month}-07T10:00:00"),  # excluded from net
    ]
    con.executemany("INSERT INTO sales VALUES (?,?,?,?,?,?)", rows)
    con.commit()
    con.close()


def test_query_survival_excludes_refunds():
    q = _load(ROOT / "db/query.py", "query")
    with tempfile.TemporaryDirectory() as d:
        dbp = Path(d) / "store.db"
        _seed_sales_db(str(dbp))
        con = sqlite3.connect(str(dbp))
        con.row_factory = sqlite3.Row
        os.environ["AGENT_MONTHLY_TARGET_EUR"] = "58"
        buf = io.StringIO()
        with redirect_stdout(buf):
            q.cmd_survival(con)
        out = buf.getvalue()
        con.close()
    # 2 non-refunded x €9.99 = €19.98 net (the €9.99 refund must NOT count)
    assert "€  19.98" in out or "19.98" in out, f"net revenue wrong:\n{out}"
    assert "AT RISK" in out, "should be AT RISK below €58 target"


# ── Gumroad CLI integration boundary ───────────────────────────────────────
def test_sync_cli_json_uses_machine_safe_flags():
    sync = _load(ROOT / "db/sync.py", "sync_cli_test")
    completed = type("Result", (), {
        "returncode": 0,
        "stdout": '{"success":true,"sales":[]}',
        "stderr": "",
    })()
    with patch.object(sync.subprocess, "run", return_value=completed) as run:
        data = sync.cli_json("sales", "list", "--all")
    command = run.call_args.args[0]
    assert command[:4] == ["gumroad", "sales", "list", "--all"]
    assert command[-3:] == ["--json", "--no-input", "--no-color"]
    assert data["success"] is True


def test_workspace_gumroad_code_has_no_direct_api_calls():
    paths = [ROOT / "db/sync.py", ROOT / "scripts/download_files.py"]
    paths.extend((ROOT / "scripts/api").glob("*.sh"))
    paths.extend([ROOT / "scripts/upload_cover.py", ROOT / "scripts/upload_thumbnails.py"])
    forbidden = ("api.gumroad.com", "access_token=", "gumroad_get", "gumroad_post", "gumroad_put")
    for path in paths:
        content = path.read_text()
        for marker in forbidden:
            assert marker not in content, f"{path.name} contains direct API marker {marker}"


# ── funnel + launch_kit + real-spec build ───────────────────────────────────
def _seed_funnel_db(path, with_snapshots=True):
    con = sqlite3.connect(path)
    con.execute("CREATE TABLE products (id TEXT, name TEXT, price_cents INT, "
                "sales_count INT, sales_usd_cents REAL)")
    con.executemany("INSERT INTO products VALUES (?,?,?,?,?)",
                    [("a", "Prompt Pack", 999, 0, 0), ("b", "Notion Kit", 799, 0, 0)])
    if with_snapshots:
        con.execute("CREATE TABLE product_snapshots (id INTEGER PRIMARY KEY AUTOINCREMENT, "
                    "product_id TEXT, name TEXT, price_cents INT, sales_count INT, "
                    "sales_usd_cents REAL, published INT, snapshot_at TEXT)")
    con.commit()
    con.close()


def test_funnel_reach_verdict_when_zero_sales():
    q = _load(ROOT / "db/query.py", "query")
    with tempfile.TemporaryDirectory() as d:
        dbp = Path(d) / "store.db"
        _seed_funnel_db(str(dbp))
        con = sqlite3.connect(str(dbp))
        con.row_factory = sqlite3.Row
        buf = io.StringIO()
        with redirect_stdout(buf):
            q.cmd_funnel(con)
        con.close()
    out = buf.getvalue()
    assert "Funnel & Catalog Health" in out
    assert "Bottleneck = REACH" in out, "0-sales catalog should give the REACH verdict"


def test_funnel_tolerates_db_without_snapshots_table():
    q = _load(ROOT / "db/query.py", "query")
    with tempfile.TemporaryDirectory() as d:
        dbp = Path(d) / "store.db"
        _seed_funnel_db(str(dbp), with_snapshots=False)
        con = sqlite3.connect(str(dbp))
        con.row_factory = sqlite3.Row
        buf = io.StringIO()
        with redirect_stdout(buf):
            q.cmd_funnel(con)  # must not raise on a pre-migration DB
        con.close()
    assert "Baseline building" in buf.getvalue()


def test_launch_kit_covers_all_channels():
    lk = _load(ROOT / "scripts/launch_kit.py", "launch_kit")
    p = {"name": "75 Power Prompts for AI Masters", "formatted_price": "€7.99",
         "short_url": "https://schephenk.gumroad.com/l/x", "sales_count": 0}
    kit = lk.build_kit(p)
    for section in ("Reddit", "Product Hunt", "SEO", "Email", "Twitter"):
        assert section in kit, f"launch kit missing {section}"
    assert "LAUNCH30" in kit and p["short_url"] in kit
    subs, _ = lk.channels_for(p["name"])
    assert "r/ChatGPT" in subs, "prompt product should map to AI subreddits"


def test_builder_builds_real_lead_magnet_spec():
    spec = json.loads((ROOT / "agent/specs/free-ai-quickstart.spec.json").read_text())
    assert pb.validate_spec(spec) == [], "shipped lead-magnet spec must be valid"
    html = pb.build_html(spec)
    assert "AI Quick-Start Pack" in html and "Chapter 04" in html


# ── runner ──────────────────────────────────────────────────────────────────
def _run():
    tests = [v for k, v in sorted(globals().items())
             if k.startswith("test_") and callable(v)]
    passed = failed = 0
    for t in tests:
        try:
            t()
            print(f"  PASS  {t.__name__}")
            passed += 1
        except AssertionError as e:
            print(f"  FAIL  {t.__name__}: {e}")
            failed += 1
        except Exception as e:
            print(f"  ERROR {t.__name__}: {type(e).__name__}: {e}")
            failed += 1
    print(f"\n{passed} passed, {failed} failed")
    return failed


if __name__ == "__main__":
    sys.exit(1 if _run() else 0)
