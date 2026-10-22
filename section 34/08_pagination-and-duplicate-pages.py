# ============================================================
# FILE: 08_pagination-and-duplicate-pages.py
# TOPIC: Pagination with Stop Conditions
# ============================================================
# STUDY GUIDE
# Predict before running. Uncomment individual example calls.
# Expected outputs appear in comments. Complete the exercises yourself.
# Terminal commands are comments: run them in a terminal, not Python.

# LESSON OBJECTIVES
# 1. Follow next links using offline pages.
# 2. Prevent cycles and bound page counts.

from urllib.parse import urljoin


def collect_titles(pages, start_url, max_pages=10):
    from bs4 import BeautifulSoup

    titles = []
    visited = set()
    url = start_url
    while url and url not in visited and len(visited) < max_pages:
        if url not in pages:
            raise ValueError(f"No fixture for {url}")
        visited.add(url)
        soup = BeautifulSoup(pages[url], "html.parser")
        titles.extend(tag.get_text(" ", strip=True) for tag in soup.select("h2"))
        next_link = soup.select_one("a.next[href]")
        url = urljoin(url, next_link["href"]) if next_link else None
    return titles


def example_offline_pagination():
    pages = {
        "https://catalog.example/1": '<h2>Signals</h2><a class="next" href="/2">Next</a>',
        "https://catalog.example/2": '<h2>Blue</h2><a class="next" href="/1">Next</a>',
    }
    print(collect_titles(pages, "https://catalog.example/1"))
    # => ['Signals', 'Blue']
    print(collect_titles(pages, "https://catalog.example/1", max_pages=1))
    # => ['Signals']


# example_offline_pagination()
# The dictionary replaces HTTP; only explicitly supplied URLs are available.
# A live version also needs origin checks, request limits, and delays.
# visited prevents duplicate pages, not duplicate records across pages.
# Record deduplication needs a stable identifier such as a product URL/id.

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Why does the link back to page 1 not create an infinite loop?
# ANSWER / CODE: ______________________________________________
# 2. Remove the final next link and predict the result.
# ANSWER / CODE: ______________________________________________
# 3. Add duplicate album records and deduplicate using an explicit key.
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: Every pagination loop needs clear stopping rules.

# ============================================================
# END OF LESSON
# ============================================================

