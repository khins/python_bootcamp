# ============================================================
# FILE: 04_pagination.py
# TOPIC: Bound Paginated Retrieval
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call at a time.
# Expected results appear beside examples. Timing/order may vary where noted.
# Complete the practice yourself; example solutions are separate from practice.
# See learning-guide.txt for section order, setup, and project instructions.

# LESSON OBJECTIVES
# 1. Follow page tokens.
# 2. Detect loops and duplicate identifiers.

# SECTION 1 - UNDERSTAND THE IDEA
# Pagination splits a result across requests. APIs differ: page numbers, cursors,
# and next links are not interchangeable. This fixture uses positive integer
# page tokens. Limit pages and records, reject repeated page tokens, and choose
# a duplicate-id policy. Do not blindly forward authentication to a next URL
# on a different host. The project uses page integers rather than arbitrary URLs.

# SECTION 2 - WORKED EXAMPLES
def example_pages():
    pages = {1: {"items": ["Signals"], "next": 2},
             2: {"items": ["Blue"], "next": None}}
    page, visited, titles = 1, set(), []
    while page is not None:
        if page in visited or len(visited) >= 5:
            raise ValueError("pagination loop or limit")
        visited.add(page)
        payload = pages[page]
        titles.extend(payload["items"])
        page = payload["next"]
    print(titles)  # => ['Signals', 'Blue']

# example_pages()

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Make page 2 point back to page 1 and verify a clear error.
# ANSWER / CODE: ______________________________________________
# 2. Add a maximum record count.
# ANSWER / CODE: ______________________________________________
# 3. Choose a policy for the same id appearing on two pages.
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: Pagination is a bounded traversal, not an unguarded while loop.

# ============================================================
# END OF LESSON
# ============================================================
