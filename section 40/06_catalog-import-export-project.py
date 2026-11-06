# ============================================================
# FILE: 06_catalog-import-export-project.py
# TOPIC: Project: Catalog Importer and Exporter
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call at a time.
# Expected results appear beside examples. Timing/order may vary where noted.
# Complete the practice yourself; example solutions are separate from practice.
# See learning-guide.txt for section order, setup, and project instructions.

# LESSON OBJECTIVES
# 1. Round-trip both JSON and CSV.
# 2. Validate before replacing destination contents.

# SECTION 1 - UNDERSTAND THE IDEA
# catalog_io.py contains a complete small implementation. It supports a flat
# album schema with title, artist, and year; nested tracks belong in JSON or a
# separate CSV table. All sample files below live in an automatically cleaned
# temporary directory. A validated write can still fail mid-write; atomic
# replacement is a useful extension rather than a guarantee of this example.

# SECTION 2 - WORKED EXAMPLES
from pathlib import Path
from tempfile import TemporaryDirectory

def example_round_trip():
    from catalog_io import save_json, load_json, save_csv, load_csv
    rows = [{"title": "Live, Again", "artist": "Demo Band", "year": 2000}]
    with TemporaryDirectory() as folder:
        root = Path(folder)
        save_json(root / "catalog.json", rows)
        save_csv(root / "catalog.csv", rows)
        print(load_json(root / "catalog.json") == rows)  # => True
        print(load_csv(root / "catalog.csv") == rows)    # => True
        save_json(root / "empty.json", [])
        print(load_json(root / "empty.json"))            # => []

# example_round_trip()

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Implement your own importer with record-number errors.
# ANSWER / CODE: ______________________________________________
# 2. Verify malformed input does not truncate an existing destination.
# ANSWER / CODE: ______________________________________________
# 3. Extend the JSON schema to tracks and document the CSV flattening policy.
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: Translate, validate, and round-trip representative edge cases.

# ============================================================
# END OF LESSON
# ============================================================
