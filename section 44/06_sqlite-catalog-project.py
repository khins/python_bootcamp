# ============================================================
# FILE: 06_sqlite-catalog-project.py
# TOPIC: Project: Persist a Music Catalog
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call at a time.
# Expected results appear beside examples. Timing/order may vary where noted.
# Complete the practice yourself; example solutions are separate from practice.
# See learning-guide.txt for section order, setup, and project instructions.

# LESSON OBJECTIVES
# 1. Reopen a file-backed database.
# 2. Verify durability and validation.

# SECTION 1 - UNDERSTAND THE IDEA
# The worked core in catalog_db.py separates connection setup, schema creation,
# write operations, and ordered queries. The caller owns transactions. This demo
# creates the schema once, writes a catalog, closes, and reopens the same file.
# TemporaryDirectory keeps all practice data disposable.

# SECTION 2 - WORKED EXAMPLES
from pathlib import Path
from tempfile import TemporaryDirectory
from contextlib import closing

def example_persistence():
    from catalog_db import connect, create_schema, add_album, list_albums
    with TemporaryDirectory() as folder:
        path = Path(folder) / "music.sqlite3"
        with closing(connect(path)) as db:
            create_schema(db)
            with db:
                add_album(db, "Yes", "Fragile", 1971)
        with closing(connect(path)) as db:
            print(list_albums(db))  # => [('Yes', 'Fragile', 1971)]

# example_persistence()

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Build a CLI to add, list, and delete albums by id.
# ANSWER / CODE: ______________________________________________
# 2. Test duplicate albums, invalid years, rollback, and reopening.
# ANSWER / CODE: ______________________________________________
# 3. Add tracks linked to albums and query total synthetic duration per album.
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: Keep storage lifetime, transaction boundaries, and queries explicit.

# ============================================================
# END OF LESSON
# ============================================================
