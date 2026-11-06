# ============================================================
# FILE: 02_csv-records.py
# TOPIC: Read and Write CSV Records
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call at a time.
# Expected results appear beside examples. Timing/order may vary where noted.
# Complete the practice yourself; example solutions are separate from practice.
# See learning-guide.txt for section order, setup, and project instructions.

# LESSON OBJECTIVES
# 1. Use DictReader and DictWriter.
# 2. Convert text fields explicitly.

# SECTION 1 - UNDERSTAND THE IDEA
# CSV is a table format, not a nested-object format. Use the csv module so
# commas and quotes inside fields are escaped correctly. Reader values are
# strings; convert numbers and validate them yourself. When opening disk files,
# use encoding="utf-8" and newline="" so csv controls newline handling.

# SECTION 2 - WORKED EXAMPLES
import csv
from io import StringIO

def example_csv():
    with StringIO(newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=["title", "year"])
        writer.writeheader()
        writer.writerow({"title": "Live, Again", "year": 2000})
        stream.seek(0)
        rows = list(csv.DictReader(stream))
    print(rows)  # => [{'title': 'Live, Again', 'year': '2000'}]
    print(int(rows[0]["year"]) + 1)  # => 2001

# example_csv()

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Write a title containing both a comma and a quote.
# ANSWER / CODE: ______________________________________________
# 2. Explain why splitting each line on commas loses information.
# ANSWER / CODE: ______________________________________________
# 3. Reject missing headers and invalid year strings.
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: CSV handles escaping; your application handles field meaning.

# ============================================================
# END OF LESSON
# ============================================================
