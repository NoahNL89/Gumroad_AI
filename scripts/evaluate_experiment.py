#!/usr/bin/env python3
"""Date-gated, deterministic evaluation for the active growth experiment."""
import argparse
import json
import sqlite3
import sys
from datetime import date, datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EXPERIMENT_PATH = ROOT / "agent" / "growth_experiments.json"
DB_PATH = ROOT / "db" / "store.db"
sys.path.insert(0, str(ROOT / "scripts"))
from campaign_report import collect  # noqa: E402
from pushover_notify import send_once  # noqa: E402


def load_experiments():
    return json.loads(EXPERIMENT_PATH.read_text())


def gate(data, today=None):
    today = today or datetime.now(timezone.utc).date()
    active = data.get("active") or {}
    evaluate_on = active.get("evaluate_on")
    if not evaluate_on:
        return {"state": "no_active_date", "due": False}
    due_date = date.fromisoformat(evaluate_on)
    return {
        "experiment": active.get("id"),
        "status": active.get("status"),
        "evaluate_on": evaluate_on,
        "today": today.isoformat(),
        "days_until_evaluation": (due_date - today).days,
        "due": today >= due_date and active.get("status") == "running",
        "state": "due" if today >= due_date else "collecting",
    }


def choose_decision(report, targets, manual_analytics):
    posts_ok = report["tracked_posts"] >= targets.get("tracked_social_posts_min", 0)
    leads_ok = report["free_downloads"] >= targets.get("free_downloads_min", 0)
    sales_ok = report["paid_sales"] >= targets.get("paid_sales_min", 0)
    revenue_ok = report["gross_revenue_eur"] >= targets.get("revenue_eur_min", 0)

    if posts_ok and leads_ok and sales_ok and revenue_ok:
        outcome = "validated"
        next_action = "Keep the offer stable and run a channel/message scaling experiment."
        rationale = "The campaign met every configured success signal."
    elif report["free_downloads"] > 0 and report["paid_sales"] == 0:
        outcome = "bridge_problem"
        next_action = "Test one stronger free-to-paid bridge while keeping the product and price stable."
        rationale = "The campaign generated leads but no paid sale."
    elif report["paid_sales"] > 0 and report["bundle_sales"] == 0:
        outcome = "core_validated_upgrade_unproven"
        next_action = "Keep the core offer stable and test one toolkit-upgrade message."
        rationale = "The core product sold, but the higher-order-value upgrade did not."
    elif not posts_ok:
        outcome = "insufficient_distribution"
        next_action = "Run another focused distribution experiment before changing the product or price."
        rationale = "The campaign did not reach its minimum tracked-post sample."
    else:
        views = manual_analytics.get("gumroad_utm_page_views")
        outcome = "reach_or_message_problem"
        next_action = "Test one new qualified channel or hook; do not add another product."
        rationale = (
            "The campaign reached its posting sample but produced no measurable lead or sale."
            if views is None
            else f"The campaign recorded {views} UTM page views without enough downstream conversion."
        )

    return {
        "outcome": outcome,
        "rationale": rationale,
        "next_action": next_action,
        "page_view_data_available": manual_analytics.get("gumroad_utm_page_views") is not None,
    }


def evaluate(today=None, force=False):
    data = load_experiments()
    status = gate(data, today=today)
    active = data.get("active") or {}
    if active.get("status") != "running":
        status["message"] = "Experiment is not running; no update made."
        return status
    if not status.get("due") and not force:
        status["message"] = "Experiment is still collecting data; no update made."
        return status
    if not DB_PATH.exists():
        raise RuntimeError("db/store.db missing; run python3 db/sync.py first")

    with sqlite3.connect(DB_PATH) as con:
        report = collect(con, active["started_at"])
    actuals = {
        "evaluated_at": datetime.now(timezone.utc).isoformat(),
        "tracked_posts": report["tracked_posts"],
        "free_downloads": report["free_downloads"],
        "core_sales": report["core_sales"],
        "bundle_sales": report["bundle_sales"],
        "paid_sales": report["paid_sales"],
        "gross_revenue_eur": report["gross_revenue_eur"],
        "audience": report["audience"],
    }
    active["actuals"] = actuals
    active["decision"] = choose_decision(
        report, active.get("success_signals", {}), active.get("manual_analytics", {})
    )
    active["status"] = "evaluated"
    tmp = EXPERIMENT_PATH.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    tmp.replace(EXPERIMENT_PATH)
    decision = active["decision"]
    try:
        send_once(
            f"experiment_evaluated:{active['id']}",
            f"Growth experiment evaluated · {active['id']}",
            f"{decision['outcome']}: {decision['rationale']}\nNext: {decision['next_action']}",
            priority=1 if actuals["paid_sales"] == 0 else 0,
            url="https://schephenk.gumroad.com",
            url_title="Open store",
        )
    except RuntimeError as exc:
        print(f"Warning: experiment Pushover notification failed: {exc}", file=sys.stderr)
    return {
        **status,
        "state": "evaluated",
        "actuals": actuals,
        "decision": active["decision"],
        "message": "Experiment evaluated and saved.",
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--status", action="store_true", help="show the date gate without writing")
    parser.add_argument("--force", action="store_true", help="evaluate before the configured date")
    args = parser.parse_args(argv)
    result = gate(load_experiments()) if args.status else evaluate(force=args.force)
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
