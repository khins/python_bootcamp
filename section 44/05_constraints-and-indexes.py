# ============================================================
# FILE: 05_constraints-and-indexes.py
# TOPIC: Protect Data and Speed Lookups
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call at a time.
# Expected results appear beside examples. Timing/order may vary where noted.
# Complete the practice yourself; example solutions are separate from practice.
# See learning-guide.txt for section order, setup, and project instructions.

# LESSON OBJECTIVES
# 1. Use UNIQUE, NOT NULL, and CHECK.
# 2. Inspect an index-assisted query plan.

# SECTION 1 - UNDERSTAND THE IDEA
# Constraints protect data even when another code path writes it. An index
# accelerates some lookups but consumes disk/memory and makes writes costlier.
# EXPLAIN QUERY PLAN shows a plan, not measured runtime. Planner text can vary;
# small tables may not benefit measurably. Application validation still improves
# messages, while constraints provide a final database boundary.

# SECTION 2 - WORKED EXAMPLES
from contextlib import closing

def example_index():
    from catalog_db import connect, create_schema
    with closing(connect()) as db:
        create_schema(db)
        indexes = db.execute("PRAGMA index_list('albums')").fetchall()
        print(any(row[1] == "albums_year_idx" for row in indexes))  # => True
        plan = db.execute("EXPLAIN QUERY PLAN SELECT title FROM albums WHERE year = ?", (1982,)).fetchall()
        for row in plan:
            print(row[3])  # Plan wording varies; inspect use of albums_year_idx.

# example_index()

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Trigger each supplied constraint with a bad insert.
# ANSWER / CODE: ______________________________________________
# 2. Compare plans with and without an index in a temporary database.
# ANSWER / CODE: ______________________________________________
# 3. Explain why indexing every column is not free.
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: Constraints preserve integrity; indexes trade write/storage cost for reads.

# ============================================================
# END OF LESSON
# ============================================================
