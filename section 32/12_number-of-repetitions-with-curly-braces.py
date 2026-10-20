# ============================================================
# FILE: 12_number-of-repetitions-with-curly-braces.py
# TOPIC: Repetition Counts with Curly Braces
# ============================================================
# STUDY GUIDE
# Predict before running. Uncomment individual example calls.
# Expected outputs appear in comments. Complete the exercises yourself.

import re


# LESSON OBJECTIVES
# 1. Repeat a pattern an exact or bounded number of times.
# 2. Distinguish repetitions within a match from the number of matches.
# 3. Apply quantifiers to single characters or grouped sequences.


# ============================================================
# SECTION 1 — EXACTLY n REPETITIONS: {n}
# ============================================================
def example_exact_count():
    text = "IDs: 12 345 6789"
    print(re.findall(r"[0-9]{3}", text)) # => ['345', '678']
    print(re.fullmatch(r"[0-9]{3}", "345") is not None) # => True
    print(re.fullmatch(r"[0-9]{3}", "6789") is None)    # => True


# example_exact_count()
# {3} repeats the preceding pattern three times IN EACH match.
# It does not request three separate matches from findall().
# An unrestricted search can match three digits inside a longer number.
# Use fullmatch when the entire input must be exactly three digits.


# ============================================================
# SECTION 2 — BOUNDED AND OPEN-ENDED COUNTS
# ============================================================
def example_count_ranges():
    print(re.findall(r"a{2,4}", "a aa aaa aaaaa")) # => ['aa', 'aaa', 'aaaa']
    print(re.findall(r"a{2,}", "a aa aaaaa"))      # => ['aa', 'aaaaa']
    print(re.fullmatch(r"a{0,2}", "") is not None) # => True


# example_count_ranges()
# {m,n}: at least m and at most n, inclusive.
# {m,}: at least m, with no fixed upper bound.
# {0,n}: up to n; zero repetitions are allowed.
# Do not insert spaces into the count syntax, such as {2, 4}.
# Repetition is greedy by default: try as many as allowed while still
# permitting the rest of the pattern to match.


# ============================================================
# SECTION 3 — THE QUANTIFIER APPLIES TO THE PRECEDING UNIT
# ============================================================
def example_grouped_repetition():
    print(re.fullmatch(r"ab{3}", "abbb") is not None) # => True
    print(re.fullmatch(r"(?:ab){3}", "ababab") is not None) # => True
    print(re.findall(r"(?:ab){2}", "abab ab")) # => ['abab']


# example_grouped_repetition()
# ab{3} repeats only b. (?:ab){3} repeats the whole sequence ab.
# (?:...) is a noncapturing group: it groups without changing findall
# results into captured-group strings or tuples.
# Patterns allowing zero repetitions can yield empty matches. A successful
# zero-length Match is different from None.


# ============================================================
# SECTION 4 — PRACTICE AND FINAL REVIEW
# ============================================================
# EXERCISE: How many digits does [0-9]{2,4} allow in a full match? _
# CHALLENGE: Validate a code containing two uppercase ASCII letters,
# a hyphen, and four digits. Use fullmatch and test short/long inputs.
# Write your code here:
#
# 1. Does {3} mean three separate search results? _______________
# 2. What is the difference between ab{2} and (?:ab){2}? _________
# 3. Why can search accept part of an overlong number? __________
# KEY TAKEAWAY: Braces control repetitions inside each match;
# use fullmatch when the total input must obey that length rule.

# ============================================================
# END OF LESSON
# ============================================================

