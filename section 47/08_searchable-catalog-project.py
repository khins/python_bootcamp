# ============================================================
# FILE: 08_searchable-catalog-project.py
# TOPIC: Project: Searchable Catalog and Cost Comparison
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call at a time.
# Expected results appear beside examples. Timing/order may vary where noted.
# Complete the practice yourself; example solutions are separate from practice.
# See learning-guide.txt for section order, setup, and project instructions.

# LESSON OBJECTIVES
# 1. Compare scanning with an index.
# 2. Measure build cost separately from query cost.

# SECTION 1 - UNDERSTAND THE IDEA
# An id dictionary offers expected O(1) lookup after O(n) construction and O(n)
# extra storage; worst cases and hashing costs still exist. A linear scan needs
# no extra index but costs O(n) per worst-case query. IDs must be unique or a
# plain dictionary silently keeps one row. Measurements vary; verify answers
# before timing and include index construction when it belongs to the workload.

# SECTION 2 - WORKED EXAMPLES
from timeit import repeat
import tracemalloc

def scan(rows, identifier):
    return next((row for row in rows if row["id"] == identifier), None)

def make_index(rows):
    result = {}
    for row in rows:
        if row["id"] in result:
            raise ValueError("duplicate id")
        result[row["id"]] = row
    return result

def example_search_project():
    rows = [{"id": n, "title": f"Album {n}"} for n in range(2000)]
    index = make_index(rows)
    assert scan(rows, 1999) == index.get(1999)
    assert scan(rows, -1) == index.get(-1)
    for label, operation in [("scan", lambda: scan(rows, 1999)),
                             ("indexed", lambda: index.get(1999)),
                             ("build", lambda: make_index(rows))]:
        print(label, min(repeat(operation, number=20, repeat=3)))  # Seconds vary.
    tracemalloc.start()
    extra_index = make_index(rows)
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    print(len(extra_index), peak >= current)  # => 2000 True
    print("index traced peak bytes:", peak)  # Not total process memory; varies.

# example_search_project()

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Compare one query versus 1000 queries including index build time.
# ANSWER / CODE: ______________________________________________
# 2. Add duplicate-id and empty-catalog checks.
# ANSWER / CODE: ______________________________________________
# 3. Compare a sorted-id/bisect index and document time and extra memory.
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: Choose an index based on query volume, update needs, and storage cost.

# ============================================================
# END OF LESSON
# ============================================================
