# ============================================================
# FILE: 10_save-records-to-json-and-csv.py
# TOPIC: Saving Scraped Records
# ============================================================
# STUDY GUIDE
# Predict before running. Uncomment individual example calls.
# Expected outputs appear in comments. Complete the exercises yourself.
# Terminal commands are comments: run them in a terminal, not Python.

# LESSON OBJECTIVES
# 1. Export structured records.
# 2. Use explicit encoding and preserve field order.

# SECTION 1 — JSON PRESERVES COMMON VALUE TYPES
import csv
import io
import json


def example_json_export():
    records = [{"title": "Signals", "artist": "Rush", "year": 1982},
               {"title": "Blue", "artist": None, "year": None}]
    text = json.dumps(records, ensure_ascii=False, indent=2)
    restored = json.loads(text)
    print(restored == records)  # => True
    print(restored[1]["year"] is None)  # => True
    # JSON uses null in text; json.loads converts it back to Python None.


# example_json_export()

# SECTION 2 — CSV IS TABULAR TEXT
def example_csv_export():
    output = io.StringIO(newline="")
    writer = csv.DictWriter(output, fieldnames=["title", "artist", "year"])
    writer.writeheader()
    writer.writerow({"title": "Signals", "artist": "Rush", "year": 1982})
    print(output.getvalue().strip())
    # => title,artist,year
    # => Signals,Rush,1982


# example_csv_export()
# For a real file: open(path, "w", encoding="utf-8", newline="").
# csv handles quoting; do not manually join fields containing commas.
# CSV has no universal null/type system; DictReader returns strings.
# csv writes None as an empty field, losing the distinction from "".
# Lesson 12 saves into a temporary directory to avoid overwriting your work.
# These are introductory exports; structured data gets a later full section.

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Export a title containing a comma and inspect the quoting.
# ANSWER / CODE: ______________________________________________
# 2. Why does a CSV year need conversion back to int?
# ANSWER / CODE: ______________________________________________
# 3. Choose and document a missing-value convention for a CSV export.
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: Use serialization libraries and make data-loss tradeoffs explicit.

# ============================================================
# END OF LESSON
# ============================================================

