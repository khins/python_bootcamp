# ============================================================
# FILE: 12_album-catalog-project.py
# TOPIC: Project: Collect an Offline Album Catalog
# ============================================================
# STUDY GUIDE
# Predict before running. Uncomment individual example calls.
# Expected outputs appear in comments. Complete the exercises yourself.
# Terminal commands are comments: run them in a terminal, not Python.

# LESSON OBJECTIVES
# 1. Combine pagination, extraction, and validation.
# 2. Export and verify a complete result.

import json
from pathlib import Path
from tempfile import TemporaryDirectory
from urllib.parse import urljoin, urlsplit


def collect_catalog():
    from bs4 import BeautifulSoup

    fixture_dir = Path(__file__).resolve().parent / "fixtures"
    base = "https://catalog.example/"
    pages = {
        urljoin(base, "catalog-page-1.html"): fixture_dir / "catalog-page-1.html",
        urljoin(base, "catalog-page-2.html"): fixture_dir / "catalog-page-2.html",
    }
    current = urljoin(base, "catalog-page-1.html")
    visited = set()
    seen_ids = set()
    records = []
    while current and current not in visited:
        if len(visited) >= 5:
            raise ValueError("Page limit reached before completion.")
        if current not in pages:
            raise ValueError(f"Unexpected fixture URL: {current}")
        visited.add(current)
        soup = BeautifulSoup(pages[current].read_text(encoding="utf-8"), "html.parser")
        for card in soup.select("article.album"):
            album_id = card.get("data-id")
            title = card.select_one("h2")
            if not album_id or title is None or not title.get_text(strip=True):
                raise ValueError("Album is missing an id or title.")
            if album_id in seen_ids:
                continue
            seen_ids.add(album_id)
            artist = card.select_one(".artist")
            records.append({
                "id": album_id,
                "title": title.get_text(" ", strip=True),
                "artist": artist.get_text(" ", strip=True) if artist else None,
            })
        next_link = soup.select_one("a.next[href]")
        if next_link is None:
            current = None
        else:
            candidate = urljoin(current, next_link["href"])
            if urlsplit(candidate).netloc != urlsplit(base).netloc:
                raise ValueError("Next page leaves the practice site.")
            current = candidate
    return records


def example_catalog_project():
    records = collect_catalog()
    print([record["title"] for record in records])
    # => ['Moving Pictures', 'Blue', 'Kind of Blue']
    print(records[-1]["artist"] is None)  # => True
    with TemporaryDirectory() as directory:
        path = Path(directory) / "albums.json"
        path.write_text(json.dumps(records, ensure_ascii=False, indent=2), encoding="utf-8")
        restored = json.loads(path.read_text(encoding="utf-8"))
        print(restored == records)  # => True
    # The temporary output is removed on leaving the with block.


# example_catalog_project()
# This worked example never fetches live pages. The URL-to-file mapping is
# an allowlist: unknown URLs cannot be loaded, even on the same origin.
# CHALLENGE — YOUR OWN VERSION
# 1. Add year extraction using the policy from lesson 06.
# 2. Return a rejected-record count instead of raising for missing titles.
# 3. Export CSV as well as JSON.
# 4. Test a repeated page, duplicate record, missing artist, and unknown link.
# 5. Separate page loading from extraction before considering live HTTP.
# 6. Explain where timeouts, status checks, and request limits would belong.

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Why are visited pages and seen album ids separate sets?
# ANSWER / CODE: ______________________________________________
# 2. Which album is intentionally repeated between the fixtures?
# ANSWER / CODE: ______________________________________________
# 3. Complete the challenge and test your chosen missing-data policy.
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: Combine small stages into a scraper whose behavior you can verify.

# ============================================================
# END OF LESSON
# ============================================================

