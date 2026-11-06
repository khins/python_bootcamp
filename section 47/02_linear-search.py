# ============================================================
# FILE: 02_linear-search.py
# TOPIC: Search Without an Index
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call at a time.
# Expected results appear beside examples. Timing/order may vary where noted.
# Complete the practice yourself; example solutions are separate from practice.
# See learning-guide.txt for section order, setup, and project instructions.

# LESSON OBJECTIVES
# 1. Return a missing result explicitly.
# 2. Count comparisons in a scan.

# SECTION 1 - UNDERSTAND THE IDEA
# Linear search works on unsorted data and can stop at the first match. Best
# case is constant work; worst case checks all n records. Define duplicate and
# missing-result policies. Returning None makes absence explicit instead of
# using -1 as a list index accidentally. This helper returns the first match.

# SECTION 2 - WORKED EXAMPLES
def find_title(records, title):
    for record in records:
        if record["title"] == title:
            return record
    return None

def example_scan():
    rows = [{"title": "Blue"}, {"title": "Signals"}]
    print(find_title(rows, "Signals"))  # => {'title': 'Signals'}
    print(find_title(rows, "Missing"))  # => None

# example_scan()

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Return all duplicate-title matches instead of only the first.
# ANSWER / CODE: ______________________________________________
# 2. Count comparisons for first, last, and missing titles.
# ANSWER / CODE: ______________________________________________
# 3. Compare a case-sensitive contract with a casefolded contract.
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: A scan avoids preprocessing but repeats work for repeated queries.

# ============================================================
# END OF LESSON
# ============================================================
