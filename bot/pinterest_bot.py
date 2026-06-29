#!/usr/bin/env python3
"""
Pinterest review-and-publish assistant for Schep Digital.

Usage:
    python3 bot/pinterest_bot.py auth-url
    python3 bot/pinterest_bot.py exchange "<code>"
    python3 bot/pinterest_bot.py refresh
    python3 bot/pinterest_bot.py boards
    python3 bot/pinterest_bot.py draft [product_id]
    python3 bot/pinterest_bot.py review <draft.json>
    python3 bot/pinterest_bot.py approve <draft.json>
    python3 bot/pinterest_bot.py sandbox-promote
"""
import base64
import json
import os
import random
import secrets
import sqlite3
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

ENV_PATH = Path(__file__).parent.parent / ".env"
DB_PATH = Path(__file__).parent.parent / "db" / "store.db"
DRAFT_DIR = Path(__file__).parent.parent / "agent" / "pinterest_queue"

AUTH_URL = "https://www.pinterest.com/oauth/"
DEFAULT_API_BASE = "https://api.pinterest.com/v5"

MAX_POSTS_PER_DAY = 3
DISCOUNT_CODE = "LAUNCH30"
DEFAULT_BOARD_NAME = "AI Tools & Digital Templates"
DEFAULT_REDIRECT_URI = "http://localhost:3003/pinterest/callback"
DEFAULT_SCOPES = "user_accounts:read,boards:read,boards:write,pins:read,pins:write"

TITLE_LIMIT = 100
DESCRIPTION_LIMIT = 500

GENERIC_VALUE_TEMPLATES = [
    "{name}: a practical AI workflow/template system for creators and solo operators. Instant download, {price}. Use code {code} for 30% off.",
    "Save this if you build with AI: {name}. Built for repeatable output instead of starting from a blank page. {price}, instant download. Code {code} saves 30%.",
    "A ready-to-use digital product from Schep Digital: {name}. Useful for AI workflows, productivity, and creator systems. {price}.",
]

VALUE_TEMPLATES = GENERIC_VALUE_TEMPLATES

SELL_TEMPLATES = [
    "{name} from Schep Digital. {price}, instant download. Save this Pin and use code {code} for 30% off.",
]

BUNDLE_TEMPLATES = [
    "The Complete AI Creator Toolkit bundles 10 AI systems into one download. €29.99 once, code {code} takes 30% off.",
    "10 AI creator systems in one bundle: prompts, workflows, templates, and productivity assets. Code {code} saves 30%.",
]


def load_env():
    if ENV_PATH.exists():
        for line in ENV_PATH.read_text().splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                key = k.strip()
                value = v.strip().strip('"').strip("'")
                if key not in os.environ or (not os.environ[key] and value):
                    os.environ[key] = value


def env(name, default=None):
    load_env()
    return os.environ.get(name, default)


def require_env(name):
    value = env(name)
    if not value:
        sys.exit(f"{name} not set in .env")
    return value


def api_base():
    return env("PINTEREST_API_BASE", DEFAULT_API_BASE).rstrip("/")


def use_sandbox_api():
    os.environ["PINTEREST_API_BASE"] = env("PINTEREST_SANDBOX_API_BASE", "https://api-sandbox.pinterest.com/v5")


def is_sandbox():
    return "api-sandbox.pinterest.com" in api_base()


def token_url():
    return f"{api_base()}/oauth/token"


def truncate(text, limit):
    text = " ".join(str(text).split())
    return text if len(text) <= limit else text[: limit - 3].rstrip() + "..."


def is_prompt_product(name: str) -> bool:
    n = name.lower()
    return any(k in n for k in ("prompt", "gemini", "llm", "vault"))


def api_request(method, path, data=None, token=None, auth_basic=False):
    body = None
    headers = {"User-Agent": "SchepDigitalPinterestBot/1.0"}

    if data is not None:
        if auth_basic:
            body = urllib.parse.urlencode(data).encode()
            headers["Content-Type"] = "application/x-www-form-urlencoded"
        else:
            body = json.dumps(data).encode()
            headers["Content-Type"] = "application/json"

    if token:
        headers["Authorization"] = f"Bearer {token}"

    if auth_basic:
        client_id = require_env("PINTEREST_APP_ID")
        client_secret = require_env("PINTEREST_APP_SECRET")
        raw = f"{client_id}:{client_secret}".encode()
        headers["Authorization"] = "Basic " + base64.b64encode(raw).decode()

    url = path if path.startswith("http") else f"{api_base()}{path}"
    req = urllib.request.Request(url, data=body, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            response_body = r.read().decode()
            return json.loads(response_body) if response_body else {}
    except urllib.error.HTTPError as e:
        detail = e.read().decode(errors="replace")
        raise RuntimeError(f"Pinterest API {method} {path} failed: HTTP {e.code} {detail}") from e


def auth_url():
    client_id = require_env("PINTEREST_APP_ID")
    redirect_uri = env("PINTEREST_REDIRECT_URI", DEFAULT_REDIRECT_URI)
    scopes = env("PINTEREST_SCOPES", DEFAULT_SCOPES)
    state = secrets.token_urlsafe(18)
    params = {
        "client_id": client_id,
        "redirect_uri": redirect_uri,
        "response_type": "code",
        "scope": scopes,
        "state": state,
    }
    print(AUTH_URL + "?" + urllib.parse.urlencode(params))
    print(f"\nState: {state}")
    print("After approving, copy the `code` query parameter from the redirect URL and run:")
    print('python3 bot/pinterest_bot.py exchange "<code>"')
    print("\nFor the Standard access demo, record this OAuth flow plus:")
    print("python3 bot/pinterest_bot.py sandbox-promote")


def print_token_export(data):
    print(json.dumps({
        "access_token_present": bool(data.get("access_token")),
        "refresh_token_present": bool(data.get("refresh_token")),
        "expires_in": data.get("expires_in"),
        "scope": data.get("scope"),
        "token_type": data.get("token_type"),
    }, indent=2))
    if data.get("access_token"):
        print("\nAdd/update these in .env:")
        print(f"PINTEREST_ACCESS_TOKEN={data['access_token']}")
    if data.get("refresh_token"):
        print(f"PINTEREST_REFRESH_TOKEN={data['refresh_token']}")


def exchange_code(code):
    data = api_request(
        "POST",
        token_url(),
        {
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": env("PINTEREST_REDIRECT_URI", DEFAULT_REDIRECT_URI),
        },
        auth_basic=True,
    )
    print_token_export(data)


def refresh_token():
    refresh = require_env("PINTEREST_REFRESH_TOKEN")
    data = api_request(
        "POST",
        token_url(),
        {
            "grant_type": "refresh_token",
            "refresh_token": refresh,
        },
        auth_basic=True,
    )
    print_token_export(data)


def access_token():
    if is_sandbox() and env("PINTEREST_SANDBOX_ACCESS_TOKEN"):
        return env("PINTEREST_SANDBOX_ACCESS_TOKEN")
    return require_env("PINTEREST_ACCESS_TOKEN")


def list_boards():
    token = access_token()
    data = api_request("GET", "/boards?page_size=100", token=token)
    boards = data.get("items", [])
    for board in boards:
        print(f"{board.get('id')}\t{board.get('name')}\tprivacy={board.get('privacy')}")
    if not boards:
        print("No boards returned.")
    return boards


def create_board(name):
    token = access_token()
    data = api_request(
        "POST",
        "/boards",
        {
            "name": name,
            "description": "AI tools, digital templates, creator systems, and productivity workflows from Schep Digital.",
            "privacy": "PUBLIC",
        },
        token=token,
    )
    print(f"Created board: {data.get('id')} {data.get('name')}")
    return data


def get_board_id():
    if is_sandbox() and env("PINTEREST_SANDBOX_BOARD_ID"):
        return env("PINTEREST_SANDBOX_BOARD_ID")
    configured = env("PINTEREST_BOARD_ID")
    if configured:
        return configured

    board_name = (
        env("PINTEREST_SANDBOX_BOARD_NAME")
        if is_sandbox() and env("PINTEREST_SANDBOX_BOARD_NAME")
        else env("PINTEREST_BOARD_NAME", DEFAULT_BOARD_NAME)
    )
    token = access_token()
    data = api_request("GET", "/boards?page_size=100", token=token)
    for board in data.get("items", []):
        if board.get("name", "").strip().lower() == board_name.strip().lower():
            return board.get("id")

    board = create_board(board_name)
    return board.get("id")


def log_promotion(platform, product_id, url, content):
    if not DB_PATH.exists():
        return
    with sqlite3.connect(str(DB_PATH)) as con:
        con.execute(
            "INSERT INTO promotions (platform, product_id, url, content, posted_at) VALUES (?,?,?,?,?)",
            (platform, product_id, url, content, datetime.now(timezone.utc).isoformat()),
        )


def check_rate_limit():
    if not DB_PATH.exists():
        print("DB not found — fail-closed on rate limit")
        return False
    platform = "pinterest_sandbox" if is_sandbox() else "pinterest"
    cutoff = (datetime.now(timezone.utc) - timedelta(hours=24)).isoformat()
    with sqlite3.connect(str(DB_PATH)) as con:
        count = con.execute(
            "SELECT COUNT(*) FROM promotions WHERE platform=? AND posted_at >= ?",
            (platform, cutoff),
        ).fetchone()[0]
    if count >= MAX_POSTS_PER_DAY:
        print(f"Rate limit: already posted {count}x in last 24h (max {MAX_POSTS_PER_DAY})")
        return False
    return True


def product_rows():
    if not DB_PATH.exists():
        sys.exit("DB not found. Run: python3 db/sync.py")
    with sqlite3.connect(str(DB_PATH)) as con:
        con.row_factory = sqlite3.Row
        return con.execute(
            """
            SELECT id, name, formatted_price, short_url, thumbnail_url
            FROM products
            WHERE published=1
              AND price_cents > 99
              AND short_url IS NOT NULL
              AND thumbnail_url IS NOT NULL
            """
        ).fetchall()


def choose_product(product_id=None):
    products = product_rows()
    if not products:
        sys.exit("No published paid products with thumbnail URLs found.")
    if product_id:
        product = next((p for p in products if p["id"] == product_id), None)
        if not product:
            sys.exit(f"No eligible product found for id: {product_id}")
        return product

    with sqlite3.connect(str(DB_PATH)) as con:
        con.row_factory = sqlite3.Row
        recent = con.execute(
            "SELECT product_id FROM promotions WHERE platform=? ORDER BY posted_at DESC LIMIT 5",
            ("pinterest_sandbox" if is_sandbox() else "pinterest",),
        ).fetchall()
    recent_ids = {r["product_id"] for r in recent}
    pool = [p for p in products if p["id"] not in recent_ids] or products
    bundle = next((p for p in pool if "toolkit" in p["name"].lower() or "bundle" in p["name"].lower()), None)
    return bundle if bundle and random.random() < 0.25 else random.choice(pool)


def build_pin(product):
    name = product["name"]
    url = product["short_url"]
    price = product["formatted_price"]
    is_bundle = "toolkit" in name.lower() or "bundle" in name.lower()
    template = random.choice(BUNDLE_TEMPLATES if is_bundle else VALUE_TEMPLATES)
    description = template.format(name=name, price=price, url=url, code=DISCOUNT_CODE)
    description += f" Learn more: {url}"
    return {
        "title": truncate(name, TITLE_LIMIT),
        "description": truncate(description, DESCRIPTION_LIMIT),
        "link": url,
        "media_source": {
            "source_type": "image_url",
            "url": product["thumbnail_url"],
        },
    }


def platform_name():
    return "pinterest_sandbox" if is_sandbox() else "pinterest"


def draft_path(product):
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    safe = "".join(c.lower() if c.isalnum() else "-" for c in product["name"]).strip("-")
    safe = "-".join(part for part in safe.split("-") if part)[:72] or "pin"
    return DRAFT_DIR / f"{stamp}-{safe}.json"


def write_draft(product_id=None):
    product = choose_product(product_id)
    payload = build_pin(product)
    draft = {
        "status": "needs_manual_approval",
        "created_at": datetime.now(timezone.utc).isoformat(),
        "platform": "pinterest",
        "approval_required": True,
        "approval_note": "Review title, description, link, image URL, and board before publishing. Pinterest requires specific user consent for each Pin.",
        "product": {
            "id": product["id"],
            "name": product["name"],
            "url": product["short_url"],
            "price": product["formatted_price"],
            "thumbnail_url": product["thumbnail_url"],
        },
        "pin": payload,
        "board": {
            "id_env": "PINTEREST_BOARD_ID",
            "default_name": env("PINTEREST_BOARD_NAME", DEFAULT_BOARD_NAME),
        },
    }
    DRAFT_DIR.mkdir(parents=True, exist_ok=True)
    path = draft_path(product)
    path.write_text(json.dumps(draft, indent=2) + "\n")
    print(f"Pinterest draft created: {path}")
    print_review(draft)
    print("\nPublish only after review:")
    print(f"python3 bot/pinterest_bot.py approve {path}")
    return path


def read_draft(path):
    data = json.loads(Path(path).read_text())
    if data.get("platform") != "pinterest":
        sys.exit("Draft is not a Pinterest draft.")
    pin = data.get("pin") or {}
    required = ("title", "description", "link", "media_source")
    missing = [key for key in required if not pin.get(key)]
    if missing:
        sys.exit(f"Draft missing required Pin fields: {', '.join(missing)}")
    return data


def print_review(draft):
    product = draft.get("product") or {}
    pin = draft.get("pin") or {}
    media = pin.get("media_source") or {}
    print(json.dumps({
        "status": draft.get("status"),
        "product": product.get("name"),
        "title": pin.get("title"),
        "description": pin.get("description"),
        "link": pin.get("link"),
        "image_url": media.get("url"),
        "approval_required": draft.get("approval_required", True),
    }, indent=2))


def post_payload(payload, product_id=None, product_url=None, content=None):
    if not check_rate_limit():
        return False
    board_id = get_board_id()
    if not board_id:
        sys.exit("No Pinterest board available. Set PINTEREST_BOARD_ID or allow boards:write.")
    payload = dict(payload)
    payload["board_id"] = board_id
    print(f"Posting Pinterest pin: {payload.get('title')}")
    data = api_request("POST", "/pins", payload, token=access_token())
    pin_url = data.get("link") or data.get("url") or f"https://www.pinterest.com/pin/{data.get('id')}/"
    log_promotion(platform_name(), product_id, product_url, content or payload.get("description", ""))
    print(json.dumps({"pin_id": data.get("id"), "pin_url": pin_url}, indent=2))
    return True


def post_product(product_id=None):
    product = choose_product(product_id)
    payload = build_pin(product)
    return post_payload(payload, product["id"], product["short_url"], payload["description"])


def approve_draft(path):
    draft = read_draft(path)
    print_review(draft)
    if not is_sandbox():
        print("\nManual approval recorded for this specific Pin draft.")
    product = draft.get("product") or {}
    ok = post_payload(
        draft["pin"],
        product_id=product.get("id"),
        product_url=product.get("url"),
        content=draft["pin"].get("description"),
    )
    if ok:
        draft["status"] = "published"
        draft["published_at"] = datetime.now(timezone.utc).isoformat()
        draft["published_platform"] = platform_name()
        Path(path).write_text(json.dumps(draft, indent=2) + "\n")
    return ok


def standard_access_brief():
    print("""Pinterest Standard access positioning

Use case:
Private single-user Pinterest content scheduler for Schep Digital's own Gumroad products. The tool drafts product Pins, lets the owner review title/description/link/image/board, and publishes only a specifically approved Pin.

Demo recording checklist:
1. Run `python3 bot/pinterest_bot.py auth-url` and open the OAuth URL.
2. Show Pinterest OAuth consent for the minimal scopes: user_accounts:read, boards:read, boards:write, pins:read, pins:write.
3. Exchange the returned code with `python3 bot/pinterest_bot.py exchange "<code>"`.
4. Run `python3 bot/pinterest_bot.py draft` to show the manual review draft.
5. Run `python3 bot/pinterest_bot.py sandbox-promote` to show a live sandbox Pin create API call.
6. Open Pinterest and show the sandbox-created Pin or board visible to the creator.

Production behavior:
`promote` and `draft` create review drafts only. `approve <draft.json>` is the explicit per-Pin approval command.
""")


def usage():
    print("Usage: python3 bot/pinterest_bot.py [auth-url | exchange <code> | refresh | boards | create-board [name] | draft [product_id] | review <draft.json> | approve <draft.json> | promote | post <product_id> | sandbox-boards | sandbox-promote | standard-brief]")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        usage()
        sys.exit(1)

    cmd = sys.argv[1]
    try:
        if cmd == "auth-url":
            auth_url()
        elif cmd == "exchange":
            if len(sys.argv) < 3:
                sys.exit("Provide the OAuth code from Pinterest.")
            exchange_code(sys.argv[2])
        elif cmd == "refresh":
            refresh_token()
        elif cmd == "boards":
            list_boards()
        elif cmd == "sandbox-boards":
            use_sandbox_api()
            list_boards()
        elif cmd == "create-board":
            create_board(" ".join(sys.argv[2:]) or env("PINTEREST_BOARD_NAME", DEFAULT_BOARD_NAME))
        elif cmd == "draft":
            write_draft(sys.argv[2] if len(sys.argv) >= 3 else None)
        elif cmd == "review":
            if len(sys.argv) < 3:
                sys.exit("Provide a Pinterest draft JSON path.")
            print_review(read_draft(sys.argv[2]))
        elif cmd == "approve":
            if len(sys.argv) < 3:
                sys.exit("Provide a Pinterest draft JSON path.")
            approve_draft(sys.argv[2])
        elif cmd == "promote":
            write_draft()
        elif cmd == "sandbox-promote":
            use_sandbox_api()
            post_product()
        elif cmd == "post":
            if len(sys.argv) < 3:
                sys.exit("Provide a Gumroad product id.")
            write_draft(sys.argv[2])
        elif cmd == "standard-brief":
            standard_access_brief()
        else:
            usage()
            sys.exit(1)
    except RuntimeError as e:
        sys.exit(str(e))
