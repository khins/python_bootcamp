# ============================================================
# FILE: 07_relative-links-and-url-validation.py
# TOPIC: Resolving Relative Links
# ============================================================
# STUDY GUIDE
# Predict before running. Uncomment individual example calls.
# Expected outputs appear in comments. Complete the exercises yourself.
# Terminal commands are comments: run them in a terminal, not Python.

# LESSON OBJECTIVES
# 1. Resolve links against a base URL.
# 2. Restrict navigation to the expected origin.

from urllib.parse import urldefrag, urljoin, urlsplit


def same_origin_link(base_url, href):
    if not href:
        return None
    candidate, _ = urldefrag(urljoin(base_url, href))
    base = urlsplit(base_url)
    target = urlsplit(candidate)
    if target.scheme not in {"http", "https"}:
        return None
    if (target.scheme, target.netloc) != (base.scheme, base.netloc):
        return None
    return candidate


def example_resolve_links():
    base = "https://catalog.example/albums/page-1.html"
    print(same_origin_link(base, "../artists/rush"))
    # => https://catalog.example/artists/rush
    print(same_origin_link(base, "?page=2"))
    # => https://catalog.example/albums/page-1.html?page=2
    print(same_origin_link(base, "https://elsewhere.example/"))  # => None
    print(same_origin_link(base, "mailto:someone@example.com"))  # => None
    print(same_origin_link(base, None))  # => None


# example_resolve_links()
# .example domains are illustrative; this example makes no requests.
# urljoin also accepts absolute URLs, so joining alone is not validation.
# This conservative comparison may reject equivalent differently spelled
# origins. It is a lesson-level navigation policy, not a security boundary.
# A live fetch may redirect: inspect its final URL before following links.

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Resolve '/artists/rush' and compare it with '../artists/rush'.
# ANSWER / CODE: ______________________________________________
# 2. Why should a scraper reject mailto links for page fetching?
# ANSWER / CODE: ______________________________________________
# 3. What happens when a next link points to the current page's fragment?
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: Resolve links, then apply an explicit navigation policy.

# ============================================================
# END OF LESSON
# ============================================================

