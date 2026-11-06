# ============================================================
# FILE: 02_crud-and-parameters.py
# TOPIC: Create, Read, Update, Delete
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call at a time.
# Expected results appear beside examples. Timing/order may vary where noted.
# Complete the practice yourself; example solutions are separate from practice.
# See learning-guide.txt for section order, setup, and project instructions.

# LESSON OBJECTIVES
# 1. Bind values with placeholders.
# 2. Check the effect of updates and deletes.

# SECTION 1 - UNDERSTAND THE IDEA
# CRUD means create/read/update/delete. Bind values using ? and a tuple; a
# one-value tuple needs a comma. Do not format user text into SQL. Placeholders
# are for values, not arbitrary table/column names; choose identifiers from an
# allowlist. A WHERE clause limits which rows an UPDATE or DELETE affects.

# SECTION 2 - WORKED EXAMPLES
from contextlib import closing

def example_crud():
    from catalog_db import connect, create_schema
    with closing(connect()) as db:
        create_schema(db)
        with db:
            db.execute("INSERT INTO artists(name) VALUES (?)", ("Guns N' Roses",))
            db.execute("UPDATE artists SET name = ? WHERE id = ?", ("Demo Band", 1))
        print(db.execute("SELECT name FROM artists WHERE id = ?", (1,)).fetchone())
        # => ('Demo Band',)
        with db:
            deleted = db.execute("DELETE FROM artists WHERE id = ?", (1,))
        print(deleted.rowcount)  # => 1

# example_crud()

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Query a title containing an apostrophe using parameters.
# ANSWER / CODE: ______________________________________________
# 2. Update one album by id and verify unrelated rows stay unchanged.
# ANSWER / CODE: ______________________________________________
# 3. Explain why interpolating an ORDER BY column needs an allowlist.
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: Bind values and make mutation scope explicit.

# ============================================================
# END OF LESSON
# ============================================================
