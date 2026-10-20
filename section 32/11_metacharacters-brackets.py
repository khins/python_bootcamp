# ============================================================
# FILE: 11_metacharacters-brackets.py
# TOPIC: Character Classes with Square Brackets
# ============================================================
# STUDY GUIDE
# Predict before running. Uncomment individual example calls.
# Expected outputs appear in comments. Complete the exercises yourself.

import re


# LESSON OBJECTIVES
# 1. Match one character from a set or range.
# 2. Negate a character class.
# 3. Recognize special characters inside brackets.


# ============================================================
# SECTION 1 — A CLASS CHOOSES ONE CHARACTER
# ============================================================
def example_character_class():
    print(re.findall(r"[aeiou]", "education")) # => ['e', 'u', 'a', 'i', 'o']
    print(re.findall(r"[cb]at", "cat bat rat")) # => ['cat', 'bat']
    print(re.findall(r"[cat]", "cat")) # => ['c', 'a', 't']


# example_character_class()
# [cat] means ONE c, a, or t, not the complete word cat.
# Apply a quantifier to match several characters from the class.


# ============================================================
# SECTION 2 — RANGES AND COMBINATIONS
# ============================================================
def example_ranges():
    text = "A1 b2 Z9"
    print(re.findall(r"[A-Z]", text)) # => ['A', 'Z']
    print(re.findall(r"[0-9]", text)) # => ['1', '2', '9']
    print(re.findall(r"[A-Za-z0-9]+", text)) # => ['A1', 'b2', 'Z9']


# example_ranges()
# [A-Za-z] covers ASCII letters. Avoid [A-z]: that character range
# also contains punctuation between uppercase Z and lowercase a.
# Ranges follow character ordering, not a language's alphabet rules.


# ============================================================
# SECTION 3 — NEGATION WITH A LEADING CARET
# ============================================================
def example_negated_class():
    print(re.findall(r"[^0-9]+", "A12 B3!")) # => ['A', ' B', '!']
    print(re.fullmatch(r"[^x]", "\n") is not None) # => True


# example_negated_class()
# ^ immediately after [ means any character NOT in the class.
# A negated class can match newline unless newline is excluded explicitly.
# Outside brackets, ^ has another meaning: an anchor at the start.


# ============================================================
# SECTION 4 — SPECIAL CHARACTERS INSIDE A CLASS
# ============================================================
def example_class_literals():
    print(re.findall(r"[-.]", "a-b.c")) # => ['-', '.']
    print(re.findall(r"[\[\]]", "[item]")) # => ['[', ']']


# example_class_literals()
# Dot is literal inside brackets. Hyphen defines a range in the middle;
# put it first/last or escape it to match a literal hyphen.
# Escape brackets when matching literal brackets for clarity.
# Backslash escapes such as \d still have meaning inside a class.


# ============================================================
# SECTION 5 — PRACTICE AND FINAL REVIEW
# ============================================================
# EXERCISE: Does [abc] require all three letters? ________________
# CHALLENGE: Extract runs of ASCII hexadecimal characters using
# [0-9A-Fa-f]+. Explain why extraction does not validate the whole input.
# Write your code here:
#
# 1. What does a leading ^ inside brackets mean? _______________
# 2. Why is [A-z] usually a mistake? ___________________________
# KEY TAKEAWAY: A character class selects one character from an
# allowed set, or from its complement when the class is negated.

# ============================================================
# END OF LESSON
# ============================================================

