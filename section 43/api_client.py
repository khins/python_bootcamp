"""Offline-first client for a fictional paginated music API.
Transport contract: fetch(page) returns (status, payload, headers).
A real Requests adapter must set timeouts, check content, and map its errors.
Only GET-like reads are retried here; writes need an idempotency policy.
"""
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from time import sleep

class ApiError(Exception):
    pass

def retry_delay(raw, attempt, now=None):
    if raw is None:
        return float(2 ** attempt)
    raw = str(raw).strip()
    if raw.isdigit():
        return float(raw)
    try:
        date = parsedate_to_datetime(raw)
        if date.tzinfo is None:
            date = date.replace(tzinfo=timezone.utc)
        return max(0.0, (date - (now or datetime.now(timezone.utc))).total_seconds())
    except (ValueError, TypeError, OverflowError) as error:
        raise ApiError("invalid Retry-After") from error

def request_page(fetch, page, *, attempts=3, sleeper=sleep, max_delay=30):
    if type(attempts) is not int or not 1 <= attempts <= 5:
        raise ValueError("attempts must be between 1 and 5")
    for attempt in range(attempts):
        try:
            status, payload, headers = fetch(page)
        except (TimeoutError, ConnectionError) as error:
            if attempt == attempts - 1:
                raise ApiError("transport attempts exhausted") from error
            delay = float(2 ** attempt)
        else:
            if status == 200:
                return payload
            if status not in {429, 500, 502, 503, 504}:
                raise ApiError(f"HTTP {status}")
            if attempt == attempts - 1:
                raise ApiError(f"HTTP {status}: attempts exhausted")
            header = next((v for k, v in headers.items() if k.lower() == "retry-after"), None)
            delay = retry_delay(header, attempt)
        if delay > max_delay:
            raise ApiError("retry wait exceeds budget")
        sleeper(delay)
    raise AssertionError("unreachable")

def collect_albums(fetch, *, max_pages=10, max_records=1000, sleeper=sleep):
    if type(max_pages) is not int or max_pages < 1 or type(max_records) is not int or max_records < 0:
        raise ValueError("invalid pagination limits")
    page, seen_pages, seen_ids, results = 1, set(), set(), []
    while page is not None:
        if type(page) is not int or page <= 0:
            raise ApiError("invalid page token")
        if page in seen_pages or len(seen_pages) >= max_pages:
            raise ApiError("pagination loop or page limit")
        seen_pages.add(page)
        payload = request_page(fetch, page, sleeper=sleeper)
        if not isinstance(payload, dict) or not isinstance(payload.get("items"), list) or "next" not in payload:
            raise ApiError("invalid page shape")
        for item in payload["items"]:
            if not isinstance(item, dict):
                raise ApiError("invalid album")
            identifier, title = item.get("id"), item.get("title")
            if type(identifier) is not int or identifier <= 0 or not isinstance(title, str) or not title.strip():
                raise ApiError("invalid album")
            if identifier in seen_ids:
                raise ApiError("duplicate album id")
            if len(results) >= max_records:
                raise ApiError("record limit exceeded")
            seen_ids.add(identifier)
            results.append({"id": identifier, "title": title.strip()})
        page = payload["next"]
    return results
