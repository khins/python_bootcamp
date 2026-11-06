# ============================================================
# FILE: 03_validate-api-records.py
# TOPIC: Validate API Payloads
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call at a time.
# Expected results appear beside examples. Timing/order may vary where noted.
# Complete the practice yourself; example solutions are separate from practice.
# See learning-guide.txt for section order, setup, and project instructions.

# LESSON OBJECTIVES
# 1. Check response shape.
# 2. Reject malformed records early.

# SECTION 1 - UNDERSTAND THE IDEA
# Do not trust a successful HTTP response to match your expected schema.
# Validate required fields and types before turning external records into
# internal objects. The API used in this section is fictional and tested with
# fixtures. Its schema is {items: [{id: positive int, title: str}], next: int|null}.

# SECTION 2 - WORKED EXAMPLES
def validate_item(item):
    if not isinstance(item, dict):
        raise ValueError("item must be an object")
    identifier, title = item.get("id"), item.get("title")
    if type(identifier) is not int or identifier <= 0:
        raise ValueError("id must be a positive integer")
    if not isinstance(title, str) or not title.strip():
        raise ValueError("title is required")
    return {"id": identifier, "title": title.strip()}

def example_payload():
    print(validate_item({"id": 1, "title": " Signals "}))
    # => {'id': 1, 'title': 'Signals'}
    try:
        validate_item({"id": True, "title": "Signals"})
    except ValueError as error:
        print(error)  # => id must be a positive integer

# example_payload()

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Validate items is a list before iterating.
# ANSWER / CODE: ______________________________________________
# 2. Reject a missing title and a string id.
# ANSWER / CODE: ______________________________________________
# 3. Explain whether unknown fields should be ignored or rejected in your contract.
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: Treat parsing and validation as separate steps.

# ============================================================
# END OF LESSON
# ============================================================
