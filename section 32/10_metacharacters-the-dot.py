# ============================================================
# FILE: 10_metacharacters-the-dot.py
# TOPIC: The Dot Metacharacter
# ============================================================
# STUDY GUIDE
# Predict before running. Uncomment individual example calls.
# Expected outputs appear in comments. Complete the exercises yourself.

import re


# LESSON OBJECTIVES
# 1. Match one arbitrary character with a dot.
# 2. Recognize the default newline exception.
# 3. Escape a literal dot and preview greedy matching.


# ============================================================
# SECTION 1 — DOT MATCHES ONE CHARACTER
# ============================================================
def example_dot():
    text = "cat cot c9t c t ct"
    print(re.findall(r"c.t", text)) # => ['cat', 'cot', 'c9t', 'c t']


# example_dot()
# Dot does not mean letters only: digits, spaces, and punctuation match.
# One dot requires one character, so c.t does not match ct.
# By default, dot matches any character except newline (\n).


# ============================================================
# SECTION 2 — DOTALL ALLOWS NEWLINES
# ============================================================
def example_dotall():
    text = "a\nb"
    print(re.search(r"a.b", text) is None) # => True
    match = re.search(r"a.b", text, flags=re.DOTALL)
    print(match.group() == text) # => True


# example_dotall()
# re.DOTALL changes dot's newline behavior.
# re.MULTILINE changes line-anchor behavior; it does not make dot
# match newlines. The names refer to different regex features.


# ============================================================
# SECTION 3 — MATCH A LITERAL DOT
# ============================================================
def example_literal_dot():
    text = "a.b axb"
    print(re.findall(r"a\.b", text)) # => ['a.b']
    print(re.findall(r"a[.]b", text)) # => ['a.b']


# example_literal_dot()
# Escape dot with \. or put it inside a character class [.] where
# it is literal. Raw-string syntax alone does not make dot literal.


# ============================================================
# SECTION 4 — PREVIEW: GREEDY VERSUS LAZY REPEATS
# ============================================================
def example_greediness():
    text = "<a> <b>"
    print(re.findall(r"<.*>", text))  # => ['<a> <b>']
    print(re.findall(r"<.*?>", text)) # => ['<a>', '<b>']


# example_greediness()
# * means zero or more of the preceding pattern and is greedy by default.
# *? is lazy: it tries the shortest match that lets the rest succeed.
# Neither form is a general HTML parser. These are small text examples.


# ============================================================
# SECTION 5 — PRACTICE AND FINAL REVIEW
# ============================================================
# EXERCISE: Does r"a.b" match "ab", "a-b", or "a\nb" by default?
# ANSWER: ____________________________________________________
# CHALLENGE: Find literal ".txt" substrings in a string containing
# "notes.txt notesXtxt". Explain why the dot must be escaped.
# Write your code here:
#
# 1. How many characters does one dot consume? _________________
# 2. Which flag makes dot include newline? _____________________
# KEY TAKEAWAY: Dot is broad but not unlimited; escape it whenever
# you mean a literal period instead of an arbitrary character.

# ============================================================
# END OF LESSON
# ============================================================

