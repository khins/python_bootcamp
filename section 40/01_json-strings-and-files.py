# ============================================================
# FILE: 01_json-strings-and-files.py
# TOPIC: JSON Text and Python Values
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call at a time.
# Expected results appear beside examples. Timing/order may vary where noted.
# Complete the practice yourself; example solutions are separate from practice.
# See learning-guide.txt for section order, setup, and project instructions.

# LESSON OBJECTIVES
# 1. Distinguish dumps/loads from dump/load.
# 2. Inspect JSON type conversions.

# SECTION 1 - UNDERSTAND THE IDEA
# JSON stores objects, arrays, strings, numbers, booleans, and null. dumps makes
# a string; loads parses a string. dump/load work with file objects. A JSON
# object has string keys. Tuples become arrays and load back as lists. JSON is
# data, not Python code; never use eval to parse imported records.

# SECTION 2 - WORKED EXAMPLES
import json
from io import StringIO

def example_json():
    record = {"title": "Blue", "owned": True, "rating": None}
    text = json.dumps(record, sort_keys=True)
    print(text)  # => {"owned": true, "rating": null, "title": "Blue"}
    print(json.loads(text) == record)  # => True
    with StringIO() as stream:
        json.dump([record], stream)
        stream.seek(0)
        print(json.load(stream)[0]["title"])  # => Blue

# example_json()

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Round-trip a list of two albums.
# ANSWER / CODE: ______________________________________________
# 2. Predict the result of round-tripping a tuple.
# ANSWER / CODE: ______________________________________________
# 3. Catch JSONDecodeError for malformed text.
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: Choose the JSON function by whether you have text or an open file.

# ============================================================
# END OF LESSON
# ============================================================
