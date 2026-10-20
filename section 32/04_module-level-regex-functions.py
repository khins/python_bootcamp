# ============================================================
# FILE: 04_module-level-regex-functions.py
# TOPIC: Module-Level Regular Expression Functions
# ============================================================
# STUDY GUIDE
# Predict before running. Uncomment individual example calls.
# Expected outputs appear in comments. Complete the exercises yourself.

import re


# LESSON OBJECTIVES
# 1. Use re functions without explicitly compiling first.
# 2. Supply pattern, text, and flags in the correct places.
# 3. Preview substitution and splitting.


# ============================================================
# SECTION 1 — MODULE FUNCTIONS ACCEPT PATTERN THEN TEXT
# ============================================================
def example_module_functions():
    print(re.search(r"cat", "a cat").group()) # => cat
    print(re.match(r"cat", "a cat") is None) # => True
    print(re.fullmatch(r"cat", "cat").group()) # => cat
    print(re.findall(r"cat", "cat cat")) # => ['cat', 'cat']
    print([m.span() for m in re.finditer(r"cat", "cat cat")])
    # => [(0, 3), (4, 7)]


# example_module_functions()
# re.search(pattern_text, input_text) is the module-level form.
# compiled.search(input_text) uses an already compiled pattern.
# The re module caches recently used patterns; explicitly compiling
# is useful for named/reused patterns, not a guarantee of faster code.


# ============================================================
# SECTION 2 — FLAGS ADJUST MATCHING BEHAVIOR
# ============================================================
def example_ignore_case():
    print(re.findall(r"cat", "Cat CAT cat", flags=re.IGNORECASE))
    # => ['Cat', 'CAT', 'cat']
    pattern = re.compile(r"cat", flags=re.IGNORECASE)
    print(pattern.search("CAT").group()) # => CAT


# example_ignore_case()
# Matches retain the original input's capitalization.
# Put flags in re.compile when using a compiled pattern. A compiled
# pattern's search(text, pos) second argument is a position, not flags.


# ============================================================
# SECTION 3 — REPLACE OR SPLIT WITH A PATTERN
# ============================================================
def example_sub_and_split():
    text = "cat and cat"
    print(re.sub(r"cat", "dog", text)) # => dog and dog
    print(text)                        # => cat and cat
    print(re.split(r",", "red,green,blue")) # => ['red', 'green', 'blue']
    print(re.escape("a.b")) # => a\.b


# example_sub_and_split()
# sub returns new text; strings are immutable. split returns a list.
# re.escape prepares literal text for use inside a pattern so special
# characters are treated literally. It is not a replacement-text escaper.


# ============================================================
# SECTION 4 — PRACTICE AND FINAL REVIEW
# ============================================================
# EXERCISE: Which comes first in re.search: pattern or input? ____
# CHALLENGE: Find "python" case-insensitively in three strings.
# Write both module-level and compiled-pattern versions.
# Write your code here:
#
# 1. Does IGNORECASE lowercase the returned match? ______________
# 2. Does re.sub change the original string? ___________________
# 3. What problem does re.escape solve? ________________________
# KEY TAKEAWAY: Module functions are convenient for short tasks;
# compiled patterns make reused expressions explicit and readable.

# ============================================================
# END OF LESSON
# ============================================================

