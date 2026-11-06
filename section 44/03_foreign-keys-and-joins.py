# ============================================================
# FILE: 03_foreign-keys-and-joins.py
# TOPIC: Relate Artists and Albums
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call at a time.
# Expected results appear beside examples. Timing/order may vary where noted.
# Complete the practice yourself; example solutions are separate from practice.
# See learning-guide.txt for section order, setup, and project instructions.

# LESSON OBJECTIVES
# 1. Enforce relationships.
# 2. Join normalized tables.

# SECTION 1 - UNDERSTAND THE IDEA
# A foreign key points to a key in another table. SQLite foreign-key enforcement
# must be enabled per connection, outside an active transaction. A JOIN combines
# matching rows; LEFT JOIN also retains unmatched left rows with NULL right
# values. Joining avoids storing the artist name redundantly in every album row.

# SECTION 2 - WORKED EXAMPLES
from contextlib import closing

def example_join():
    from catalog_db import connect, create_schema, add_album, list_albums
    with closing(connect()) as db:
        create_schema(db)
        with db:
            add_album(db, "Rush", "Signals", 1982)
            add_album(db, "Rush", "Hemispheres", 1978)
        print(list_albums(db))
        # => [('Rush', 'Hemispheres', 1978), ('Rush', 'Signals', 1982)]
        print(db.execute("SELECT COUNT(*) FROM artists").fetchone()[0])  # => 1

# example_join()

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Insert an album with a missing artist id and catch IntegrityError.
# ANSWER / CODE: ______________________________________________
# 2. Write a LEFT JOIN to include artists with no albums.
# ANSWER / CODE: ______________________________________________
# 3. Explain how joining changes the result row shape.
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: Normalize shared facts and join through explicit keys.

# ============================================================
# END OF LESSON
# ============================================================
