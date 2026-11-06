# ============================================================
# FILE: 04_transactions-and-rollback.py
# TOPIC: Commit Related Changes Together
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call at a time.
# Expected results appear beside examples. Timing/order may vary where noted.
# Complete the practice yourself; example solutions are separate from practice.
# See learning-guide.txt for section order, setup, and project instructions.

# LESSON OBJECTIVES
# 1. Use a transaction as a unit of work.
# 2. Let exceptions reach the transaction boundary.

# SECTION 1 - UNDERSTAND THE IDEA
# With the helper's explicit DEFERRED isolation mode, DML starts a transaction.
# The connection context commits on normal exit and rolls back on an escaping
# exception. Catch outside the with block if failure should roll everything
# back. executescript has transaction subtleties; schema setup here is separate
# from the business transaction. Closing a connection is a separate operation.

# SECTION 2 - WORKED EXAMPLES
from contextlib import closing
import sqlite3

def example_rollback():
    from catalog_db import connect, create_schema
    with closing(connect()) as db:
        create_schema(db)
        try:
            with db:
                db.execute("INSERT INTO artists(name) VALUES (?)", ("Rush",))
                db.execute("INSERT INTO artists(name) VALUES (?)", ("Rush",))
        except sqlite3.IntegrityError:
            print("rolled back")  # => rolled back
        print(db.execute("SELECT COUNT(*) FROM artists").fetchone()[0])  # => 0

# example_rollback()

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Insert two valid rows in one transaction and verify commit.
# ANSWER / CODE: ______________________________________________
# 2. Explain what changes if the exception is caught inside with db.
# ANSWER / CODE: ______________________________________________
# 3. Design a batch import that is all-or-nothing.
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: A transaction boundary should match a meaningful unit of work.

# ============================================================
# END OF LESSON
# ============================================================
