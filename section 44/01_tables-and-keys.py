# ============================================================
# FILE: 01_tables-and-keys.py
# TOPIC: Tables, Rows, and Primary Keys
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call at a time.
# Expected results appear beside examples. Timing/order may vary where noted.
# Complete the practice yourself; example solutions are separate from practice.
# See learning-guide.txt for section order, setup, and project instructions.

# LESSON OBJECTIVES
# 1. Create an in-memory database.
# 2. Distinguish identity from row position.

# SECTION 1 - UNDERSTAND THE IDEA
# A table defines named columns; each row stores a record. A primary key uniquely
# identifies a row and is not its display position. SQLite :memory: databases
# exist for a connection lifetime. closing closes the connection; with connection
# alone manages transactions, not closure. The helper enables foreign keys.

# SECTION 2 - WORKED EXAMPLES
from contextlib import closing

def example_schema():
    from catalog_db import connect, create_schema
    with closing(connect()) as db:
        create_schema(db)
        with db:
            db.execute("INSERT INTO artists(name) VALUES (?)", ("Rush",))
        print(db.execute("SELECT id, name FROM artists").fetchall())  # => [(1, 'Rush')]

# example_schema()

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Create a tracks table with a primary key.
# ANSWER / CODE: ______________________________________________
# 2. Explain why SELECT needs ORDER BY for guaranteed ordering.
# ANSWER / CODE: ______________________________________________
# 3. Compare in-memory storage with a database path on disk.
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: Keys identify records; explicit ordering controls presentation.

# REFERENCES
# https://docs.python.org/3.13/library/sqlite3.html

# ============================================================
# END OF LESSON
# ============================================================
