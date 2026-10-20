# ============================================================
# FILE: 06_search-for-digit-and-non-digit.py
# TOPIC: Digit and Non-Digit Characters: \d and \D
# ============================================================
# STUDY GUIDE
# Predict before running. Uncomment individual example calls.
# Expected outputs appear in comments. Complete the exercises yourself.

import re


# LESSON OBJECTIVES
# 1. Match decimal digits and their complement.
# 2. Distinguish one character from a run of characters.
# 3. Recognize Unicode versus ASCII digit matching.


# ============================================================
# SECTION 1 — \d MATCHES ONE DECIMAL DIGIT
# ============================================================
def example_digits():
    text = "Room 42, floor 7"
    print(re.findall(r"\d", text))  # => ['4', '2', '7']
    print(re.findall(r"\d+", text)) # => ['42', '7']


# example_digits()
# \d matches one digit. Preview: + repeats the preceding pattern one
# or more times. Regex results are strings; convert with int if needed.


# ============================================================
# SECTION 2 — \D MATCHES ONE NON-DIGIT
# ============================================================
def example_non_digits():
    print(re.findall(r"\D", "A1 B2!")) # => ['A', ' ', 'B', '!']
    print(re.sub(r"\D", "", "(555) 123-4567")) # => 5551234567


# example_non_digits()
# \D includes letters, punctuation, whitespace, and other non-digits.
# Removing non-digits does not prove an input is a valid phone number.
# Extracting digit runs is not a general parser for signed numbers,
# decimals, scientific notation, or formatted currency.


# ============================================================
# SECTION 3 — UNICODE IS THE DEFAULT FOR str PATTERNS
# ============================================================
def example_unicode_digits():
    text = "A2 \u0663" # The last character is Arabic-Indic digit three.
    print(re.findall(r"\d", text) == ["2", "\u0663"]) # => True
    print(re.findall(r"[0-9]", text)) # => ['2']
    print(re.findall(r"\d", text, flags=re.ASCII)) # => ['2']


# example_unicode_digits()
# For str patterns, \d includes Unicode decimal digits, not just 0–9.
# [0-9] or re.ASCII makes an ASCII-only requirement explicit.
# \d does not mean every symbol that has some numeric meaning.


# ============================================================
# SECTION 4 — PRACTICE AND FINAL REVIEW
# ============================================================
# EXERCISE: What does r"\d+" find in "-12.50"? _________________
# CHALLENGE: Extract ASCII digit runs from "A12 B003 C7". Print
# the strings first, then their integer conversions. What happens to zeros?
# Write your code here:
#
# 1. Does \d alone match an entire multi-digit number? __________
# 2. Does \D include spaces? __________________________________
# 3. How can you restrict digits to ASCII? _____________________
# KEY TAKEAWAY: \d and \D classify characters, not complete
# numeric formats or validated business values.

# ============================================================
# END OF LESSON
# ============================================================

