"""Shared campaign settings and tracking helpers for Schep Digital bots."""
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

LEAD_PRODUCT_ID = "GusEpfVyj3ByGk34VFgYZA=="
LEAD_PRODUCT_NAME = "Can My Computer Run Private AI? Free Readiness Kit"
FOCUS_PRODUCT_ID = "gIXM0JN3NDuI1-2BadEVNg=="
FOCUS_PRODUCT_NAME = "Private AI on Your Computer: Local LLM Setup Guide (2026)"
BUNDLE_PRODUCT_ID = "ws-l3GFbvznUmNYUgBwUGA=="
BUNDLE_PRODUCT_NAME = "The Complete AI Creator Toolkit — 10 Practical Systems"
CAMPAIGN_PRODUCT_ID = LEAD_PRODUCT_ID
CAMPAIGN_PRODUCT_NAME = LEAD_PRODUCT_NAME
CAMPAIGN = "private_ai_free_to_paid_bridge_2026_08"
DISCOUNT_CODE = "LAUNCH30"


def tracked_url(url: str, source: str, content: str) -> str:
    """Add stable UTM attribution without discarding an existing query string."""
    parts = urlsplit(url)
    query = dict(parse_qsl(parts.query, keep_blank_values=True))
    query.update({
        "utm_source": source,
        "utm_medium": "social",
        "utm_campaign": CAMPAIGN,
        "utm_content": content,
    })
    return urlunsplit((parts.scheme, parts.netloc, parts.path, urlencode(query), parts.fragment))


def focus_product(con):
    """Return the campaign product, surviving a future ID migration by name."""
    con.row_factory = __import__("sqlite3").Row
    row = con.execute(
        "SELECT id, name, formatted_price, short_url FROM products "
        "WHERE published=1 AND id=?",
        (FOCUS_PRODUCT_ID,),
    ).fetchone()
    if row:
        return row
    return con.execute(
        "SELECT id, name, formatted_price, short_url FROM products "
        "WHERE published=1 AND lower(name) LIKE '%local llm%' LIMIT 1"
    ).fetchone()


def campaign_product(con):
    """Return the free, tightly aligned acquisition offer for this campaign."""
    con.row_factory = __import__("sqlite3").Row
    row = con.execute(
        "SELECT id, name, formatted_price, short_url FROM products "
        "WHERE published=1 AND id=?",
        (CAMPAIGN_PRODUCT_ID,),
    ).fetchone()
    if row:
        return row
    return con.execute(
        "SELECT id, name, formatted_price, short_url FROM products "
        "WHERE published=1 AND lower(name) LIKE '%private ai%readiness%' LIMIT 1"
    ).fetchone()


def next_variant(con, platform: str, product_id: str, variant_count: int) -> int:
    """Rotate campaign lessons based on already-logged posts."""
    count = con.execute(
        "SELECT COUNT(*) FROM promotions WHERE platform=? AND product_id=?",
        (platform, product_id),
    ).fetchone()[0]
    return count % variant_count
