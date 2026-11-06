# ============================================================
# FILE: 03_validate-nested-records.py
# TOPIC: Validate Imported Data
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call at a time.
# Expected results appear beside examples. Timing/order may vary where noted.
# Complete the practice yourself; example solutions are separate from practice.
# See learning-guide.txt for section order, setup, and project instructions.

# LESSON OBJECTIVES
# 1. Validate shape before accessing nested fields.
# 2. Report useful record errors.

# SECTION 1 - UNDERSTAND THE IDEA
# Parsing JSON only proves syntax. Validate container types, required fields,
# and value rules before using data. Report the record index to locate failures.
# Reject booleans when an actual integer is required. Return normalized new
# records so imported source objects are not silently modified.

# SECTION 2 - WORKED EXAMPLES
def validate_album(value):
    if not isinstance(value, dict):
        raise ValueError("album must be an object")
    title, year = value.get("title"), value.get("year")
    if not isinstance(title, str) or not title.strip():
        raise ValueError("title is required")
    if type(year) is not int or not 1800 <= year <= 2100:
        raise ValueError("year must be an integer from 1800 to 2100")
    tracks = value.get("tracks", [])
    if not isinstance(tracks, list) or any(not isinstance(t, str) or not t.strip() for t in tracks):
        raise ValueError("tracks must be nonempty strings")
    return {"title": title.strip(), "year": year, "tracks": [t.strip() for t in tracks]}

def example_validation():
    print(validate_album({"title": " Blue ", "year": 1971}))
    # => {'title': 'Blue', 'year': 1971, 'tracks': []}
    try:
        validate_album({"title": "Blue", "year": True})
    except ValueError as error:
        print(error)  # => year must be an integer from 1800 to 2100

# example_validation()

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Add a required artist string.
# ANSWER / CODE: ______________________________________________
# 2. Validate an entire list and include the failing row number.
# ANSWER / CODE: ______________________________________________
# 3. Test wrong container types, empty names, and boolean years.
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: Valid syntax is only the start of valid application data.

# ============================================================
# END OF LESSON
# ============================================================
