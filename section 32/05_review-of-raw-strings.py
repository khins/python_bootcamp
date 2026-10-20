# ============================================================
# FILE: 05_review-of-raw-strings.py
# TOPIC: Raw Strings and Regex Escapes
# ============================================================
# STUDY GUIDE
# Predict before running. Uncomment individual example calls.
# Expected outputs appear in comments. Complete the exercises yourself.

import re


# LESSON OBJECTIVES
# 1. Separate Python string parsing from regex interpretation.
# 2. Use raw string literals for readable patterns.
# 3. Match literal backslashes and metacharacters.


# ============================================================
# SECTION 1 — TWO LAYERS INTERPRET YOUR PATTERN
# ============================================================
# First Python constructs a string; then re interprets that string.
# In ordinary strings, Python interprets escapes such as \n and \t.
# A raw literal uses an r prefix to preserve backslashes for regex.
# A raw string is still an ordinary str object, not a separate type.

def example_raw_vs_normal():
    print(len("\n"))  # => 1 (a newline character)
    print(len(r"\n")) # => 2 (backslash followed by n)
    print(type(r"\n") is str) # => True
    print(re.search(r"\n", "a\nb").span()) # => (1, 2)


# example_raw_vs_normal()
# Raw syntax stops Python from interpreting \n; the regex engine
# still interprets that escape as a newline when matching.


# ============================================================
# SECTION 2 — MATCH A LITERAL BACKSLASH
# ============================================================
def example_literal_backslash():
    text = r"folder\file"
    print(re.findall(r"\\", text)) # => ['\\'] (list representation)
    print(re.findall("\\\\", text) == re.findall(r"\\", text)) # => True


# example_literal_backslash()
# The regex needs two backslashes to mean one literal backslash.
# Raw syntax expresses those two directly. An ordinary Python string
# needs four source backslashes to produce the same regex string.
# List/repr displays escape backslashes; that does not add characters.


# ============================================================
# SECTION 3 — RAW DOES NOT MEAN LITERAL TO REGEX
# ============================================================
def example_escape_metacharacter():
    print(re.findall(r"a.b", "a.b axb"))  # => ['a.b', 'axb']
    print(re.findall(r"a\.b", "a.b axb")) # => ['a.b']
    literal = "a.b"
    print(re.findall(re.escape(literal), "a.b axb")) # => ['a.b']


# example_escape_metacharacter()
# Dot is special to regex even inside a raw string. Escape it with \.
# A raw string literal cannot end with an odd number of backslashes.
# For example, a raw literal ending in a single backslash is invalid
# Python syntax; combine strings or use an ordinary escaped string.


# ============================================================
# SECTION 4 — PRACTICE AND FINAL REVIEW
# ============================================================
# EXERCISE: Why does r"\n" still match a newline in a regex? _____
# CHALLENGE: Search for the literal text "price($)" by passing it
# through re.escape. Include a similar nonmatching string in the input.
# Write your code here:
#
# 1. Is a raw string a special runtime type? ___________________
# 2. Which parser is affected by the r prefix? _________________
# 3. Does raw syntax disable regex metacharacters? ______________
# KEY TAKEAWAY: Raw strings make regex escapes easier to write;
# Python-string escaping and regex escaping remain separate layers.

# ============================================================
# END OF LESSON
# ============================================================

