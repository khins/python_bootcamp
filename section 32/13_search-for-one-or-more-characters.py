# ============================================================
# FILE: 13_search-for-one-or-more-characters.py
# TOPIC: One or More Repetitions with +
# ============================================================
# STUDY GUIDE
# Predict before running. Uncomment individual example calls.
# Expected outputs appear in comments. Complete the exercises yourself.

import re


# LESSON OBJECTIVES
# 1. Use + to collect one or more characters.
# 2. Compare +, *, and ? repetition.
# 3. Understand greedy/lazy matching and literal plus signs.


# ============================================================
# SECTION 1 — + MEANS ONE OR MORE OF THE PRECEDING UNIT
# ============================================================
def example_one_or_more():
    print(re.findall(r"[0-9]+", "A12 B3 C456")) # => ['12', '3', '456']
    print(re.findall(r"a+", "a aa baaa")) # => ['a', 'aa', 'aaa']
    print(re.fullmatch(r"a+", "") is None) # => True


# example_one_or_more()
# + is equivalent to {1,}. It requires at least one occurrence.
# It applies to a character, a character class, or a grouped sequence,
# not automatically to every character that appears before it.


# ============================================================
# SECTION 2 — COMPARE COMMON QUANTIFIERS
# ============================================================
def example_quantifiers():
    print(re.fullmatch(r"a*", "") is not None) # => True
    print(re.fullmatch(r"a+", "") is None)     # => True
    print(re.fullmatch(r"a?", "a") is not None) # => True
    print(re.fullmatch(r"a?", "aa") is None)    # => True


# example_quantifiers()
# * means zero or more; + means one or more; ? means zero or one.
# * and ? can match empty text. findall/finditer may include empty
# matches when the expression permits them, which can surprise beginners.


# ============================================================
# SECTION 3 — GREEDY DOES NOT MEAN THE REST IS IGNORED
# ============================================================
def example_greedy_and_lazy():
    print(re.search(r"a+a", "aaaa").group()) # => aaaa
    print(re.findall(r"a+", "aaaa"))  # => ['aaaa']
    print(re.findall(r"a+?", "aaaa")) # => ['a', 'a', 'a', 'a']


# example_greedy_and_lazy()
# Greedy + takes as many characters as possible while allowing the
# remainder of the pattern to succeed. It can give characters back.
# +? is the lazy form and tries the smallest successful repetition.
# A question mark after a quantifier changes greediness; by itself after
# a character/group it means that unit is optional.


# ============================================================
# SECTION 4 — MATCH A LITERAL PLUS SIGN
# ============================================================
def example_literal_plus():
    print(re.findall(r"\+", "2+3++4")) # => ['+', '+', '+']
    print(re.findall(r"\++", "2+3++4")) # => ['+', '++']


# example_literal_plus()
# In \++, the escaped first plus is literal; the second plus repeats it.
# [+] is another way to write one literal plus character.
# Prefer simple, constrained patterns over nested ambiguous repetition
# such as (a+)+, which can become very slow on failing inputs.


# ============================================================
# SECTION 5 — PRACTICE AND FINAL REVIEW
# ============================================================
# EXERCISE: Does r"ab+" match "abbb" or "abab" in full? ________
# CHALLENGE: Extract runs of ASCII letters, ignoring digits and
# punctuation. Then require an entire input to contain at least one letter
# and nothing else. Compare findall with fullmatch.
# Write your code here:
#
# 1. What is the minimum repetition count for +? ________________
# 2. How does lazy repetition (+?) differ from greedy repetition (+)? _______________
# 3. How do you match a literal plus? __________________________
# KEY TAKEAWAY: + builds nonempty runs; its target and greediness
# determine how much text each match consumes.

# ============================================================
# END OF LESSON
# ============================================================

