# ============================================================
# FILE: 07_search-for-word-and-non-word.py
# TOPIC: Word and Non-Word Characters: \w and \W
# ============================================================
# STUDY GUIDE
# Predict before running. Uncomment individual example calls.
# Expected outputs appear in comments. Complete the exercises yourself.

import re


# LESSON OBJECTIVES
# 1. Identify regex word characters.
# 2. Match word-character runs and their separators.
# 3. Avoid treating \w as a complete identifier-validation rule.


# ============================================================
# SECTION 1 — \w INCLUDES LETTERS, DIGITS, AND UNDERSCORES
# ============================================================
def example_word_characters():
    text = "user_42 says hi!"
    print(re.findall(r"\w+", text)) # => ['user_42', 'says', 'hi']
    print(re.findall(r"\w", "A_2!")) # => ['A', '_', '2']


# example_word_characters()
# For Unicode str patterns, \w includes Unicode alphanumeric characters
# and underscore. It does not mean only English letters or natural words.


# ============================================================
# SECTION 2 — \W IS THE COMPLEMENT
# ============================================================
def example_non_word_characters():
    print(re.findall(r"\W", "hi-there!")) # => ['-', '!']
    print(re.findall(r"\W+", "hi,  there!")) # => [',  ', '!']
    print(re.findall(r"\w+", "can't re-enter")) # => ['can', 't', 're', 'enter']


# example_non_word_characters()
# Spaces, punctuation, and hyphens are non-word characters.
# Apostrophes split these matches, even though a reader may see one word.
# Underscores do not split \w runs.


# ============================================================
# SECTION 3 — UNICODE AND ASCII DIFFER
# ============================================================
def example_ascii_flag():
    text = "caf\u00e9_2"
    print(re.fullmatch(r"\w+", text) is not None) # => True
    print(re.findall(r"\w+", text, flags=re.ASCII)) # => ['caf', '_2']


# example_ascii_flag()
# Under re.ASCII, \w corresponds to [a-zA-Z0-9_].
# A username policy might require a letter first or prohibit underscores.
# \w+ alone does not enforce those rules and is not equivalent to all
# the rules for Python identifiers. Use str.isidentifier() for that task.


# ============================================================
# SECTION 4 — PRACTICE AND FINAL REVIEW
# ============================================================
# EXERCISE: How many matches does \w+ find in "one_two-three"? ___
# CHALLENGE: Extract word-character runs from a sentence containing
# underscores, digits, and punctuation. Explain each split.
# Write your code here:
#
# 1. Is underscore a word character? ___________________________
# 2. Is a hyphen a word character? _____________________________
# 3. Does \w mean only letters? ________________________________
# KEY TAKEAWAY: Regex word characters are a technical category,
# not a complete definition of human words or valid usernames.

# ============================================================
# END OF LESSON
# ============================================================

