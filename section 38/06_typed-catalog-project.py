# ============================================================
# FILE: 06_typed-catalog-project.py
# TOPIC: Project: Add Hints to an Analyzer
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call at a time.
# Expected results appear beside examples. Timing/order may vary where noted.
# Complete the practice yourself; example solutions are separate from practice.
# See learning-guide.txt for section order, setup, and project instructions.

# LESSON OBJECTIVES
# 1. Annotate an existing aggregation pipeline.
# 2. Check both typing and behavior.

# SECTION 1 - UNDERSTAND THE IDEA
# Start with section 36's analyzer or your own version. Annotate the record,
# iterable input, summary output, and every helper. typed_catalog.py is a smaller
# worked reference with no third-party runtime dependencies. Run mypy on that
# file from lesson 05. Type hints describe trusted records; a later importer
# must still validate untrusted JSON before constructing those records.

# SECTION 2 - WORKED EXAMPLES
def example_project():
    from typed_catalog import summarize
    print(summarize([{"artist": "Rush", "seconds": 20},
                     {"artist": "Rush", "seconds": 30}]))  # => {'Rush': 50}
    print(summarize([]))  # => {}
    try:
        summarize([{"artist": "Rush", "seconds": -1}])
    except ValueError as error:
        print(error)  # => seconds must be a nonnegative integer

# example_project()

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Annotate your analyzer without using Any.
# ANSWER / CODE: ______________________________________________
# 2. Add a return type for a summary containing counts and totals.
# ANSWER / CODE: ______________________________________________
# 3. Record one static error and one runtime validation error and explain the difference.
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: Combine static contracts, boundary validation, and behavior checks.

# ============================================================
# END OF LESSON
# ============================================================
