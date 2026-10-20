# ============================================================
# FILE: 03_the-findall-and-finditer-methods.py
# TOPIC: Finding Multiple Matches with findall and finditer
# ============================================================
# STUDY GUIDE
# Predict before running. Uncomment individual example calls.
# Expected outputs appear in comments. Complete the exercises yourself.

import re


# LESSON OBJECTIVES
# 1. Collect non-overlapping matches.
# 2. Distinguish strings returned by findall from Match objects.
# 3. Recognize how capturing groups change findall's output.


# ============================================================
# SECTION 1 — findall(): COLLECT MATCHED TEXT
# ============================================================
def example_findall():
    pattern = re.compile(r"cat")
    print(pattern.findall("cat dog cat")) # => ['cat', 'cat']
    print(pattern.findall("dog"))         # => []


# example_findall()
# Results are returned in left-to-right order, without overlap.
# With no capturing groups, findall returns a list of complete matches.


# ============================================================
# SECTION 2 — finditer(): INSPECT EACH Match
# ============================================================
def example_finditer():
    pattern = re.compile(r"cat")
    matches = pattern.finditer("cat dog cat")
    for match in matches:
        print(match.group(), match.span())
    # => cat (0, 3)
    # => cat (8, 11)
    print(list(matches)) # => [] (the iterator was consumed)


# example_finditer()
# finditer is useful when you need locations or other match details.
# No matches means an empty iterator, not None. Call finditer again
# if you need a fresh iterator after consuming the first one.


# ============================================================
# SECTION 3 — CAPTURING GROUPS CHANGE findall RESULTS
# ============================================================
def example_capturing_groups():
    text = "A1 B2"
    print(re.findall(r"[A-Z][0-9]", text))     # => ['A1', 'B2']
    print(re.findall(r"([A-Z])[0-9]", text))   # => ['A', 'B']
    print(re.findall(r"([A-Z])([0-9])", text)) # => [('A', '1'), ('B', '2')]
    for match in re.finditer(r"([A-Z])([0-9])", text):
        print(match.group(0)) # => A1, then B2 on separate lines


# example_capturing_groups()
# Preview: parentheses capture groups; brackets select characters.
# With one capturing group findall returns that group's strings;
# with several it returns tuples. finditer still yields Match objects.


# ============================================================
# SECTION 4 — MATCHES DO NOT OVERLAP BY DEFAULT
# ============================================================
def example_nonoverlap():
    print(re.findall(r"ana", "banana")) # => ['ana']


# example_nonoverlap()
# After consuming the first "ana", scanning continues after that match.
# Overlapping searches require another technique, such as lookahead,
# beyond the scope of these introductory lessons.


# ============================================================
# SECTION 5 — PRACTICE AND FINAL REVIEW
# ============================================================
# EXERCISE: What does findall return when nothing matches? _______
# CHALLENGE: Find every "ha" in "ha ha! haha" and print each span.
# Compare the findall result with the finditer result.
# Write your code here:
#
# 1. Which method provides positions? __________________________
# 2. Can one iterator be consumed twice with the same results? ___
# KEY TAKEAWAY: Use findall for collected text and finditer for
# Match details; remember that capturing groups affect findall.

# ============================================================
# END OF LESSON
# ============================================================

