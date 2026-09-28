# Dictionary comprehensions — Study Summary
# Instructor summary:
# - A dictionary comprehension creates a new dictionary from an iterable.
# - Syntax: {key_expression: value_expression for item in iterable}
# - Add if condition at the end to include only matching items.
# - The input can be a list, a string, or another iterable.
# - The expression before the colon produces each key; the expression after it
#   produces that key's value.
# - Keys must be hashable, just like keys in any other dictionary.
# - Repeated keys replace earlier values; they do not create duplicate entries.
# - The examples below leave their input lists and strings unchanged.
# - Empty input, or a filter with no matches, produces {}.
# - String membership and comparisons are case-sensitive.
#
# Read a comprehension by identifying the iteration, then the optional filter,
# then the key and value expressions used for each included item.


# --- 1. Review a list comprehension ---
languages = ["Python", "JavaScript", "Ruby"]
length_list = [len(language) for language in languages]
print(length_list)  # [6, 10, 4]
# A list comprehension produces one element per included item.


# --- 2. Build a dictionary with a regular loop ---
lengths = {}
for language in languages:
    lengths[language] = len(language)
print(lengths)  # {'Python': 6, 'JavaScript': 10, 'Ruby': 4}
# Each language becomes a key, and its length becomes the value.


# --- 3. Express the same operation as a dictionary comprehension ---
lengths = {language: len(language) for language in languages}
print(lengths)    # {'Python': 6, 'JavaScript': 10, 'Ruby': 4}
print(languages)  # ['Python', 'JavaScript', 'Ruby']
print(type(lengths))  # <class 'dict'>
# language              -> current string from the input list
# language:             -> use that string as the key
# len(language)         -> calculate its value
# { ... } with key:value expressions creates the dictionary.
# Writing "language" instead of language would use one literal key repeatedly.


# --- 4. Filter which items become entries ---
with_t = {language: len(language) for language in languages if "t" in language}
print(with_t)  # {'Python': 6, 'JavaScript': 10}
# The filter checks for lowercase "t" in each original language name.
# Ruby does not match, so it contributes no entry.

with_uppercase_t = {
    language: len(language) for language in languages if "T" in language
}
print(with_uppercase_t)  # {}
# None of these strings contains uppercase "T".
# A comprehension can span multiple lines when that makes it easier to read.


# --- 5. Count characters by iterating over a string ---
# A short word makes it easier to check every count by hand.
word = "banana"
letter_counts = {letter: word.count(letter) for letter in word}
print(letter_counts)       # {'b': 1, 'a': 3, 'n': 2}
print(len(letter_counts))  # 3 — unique keys, not the six input characters
# The loop visits b, a, n, a, n, a.
# Each count() call counts that letter throughout the WHOLE word.
# Repeated a and n keys receive their counts again; no duplicate keys appear.
# This repeats counting work. It is a useful syntax example, but repeated
# count() calls are not an efficient counting strategy for large strings.

later_letters = {
    letter: word.count(letter) for letter in word if letter > "j"
}
print(later_letters)  # {'n': 2}
# For lowercase English letters, > "j" selects letters after j.
# More generally, string comparisons use Unicode character order, so this
# is not a universal alphabetical test across mixed cases or languages.


# --- 6. Transformed keys can collide ---
names = ["Rush", "RUSH", "Yes"]
original_names = {name.lower(): name for name in names}
print(original_names)  # {'rush': 'RUSH', 'yes': 'Yes'}
# Both Rush and RUSH produce the same key: 'rush'. The later value wins.
# Replacing a key's value does not move that key's insertion position.

empty_lengths = {name: len(name) for name in []}
print(empty_lengths)  # {}

# A loop remains a good choice when the steps are clearer on separate lines.
# A comprehension is useful when the key, value, and filter are easy to follow.


# --- 7. Practice: predict, explain, then run ---
# Write predictions in the ANSWER comments before uncommenting each exercise.
# Identify the input item, output key, output value, and optional filter.

# Exercise 1 — Map words to lengths
# Predict both outputs. Explain what goes on each side of the colon.
bands = ["Rush", "Yes", "Genesis"]
lengths = {band: len(band) for band in bands}
print(lengths)
print(bands)
# ANSWER:
# {'Rush': 4, 'Yes': 3, 'Genesis': 7}
# ["Rush", "Yes", "Genesis"]
# Explain what goes on each side of the colon: band is a str variable , and the comprehension is looping
# over the bands list while the len function is determining the length of the word looped by band

# Exercise 2 — Filter by length
# Predict both outputs. Which input names are excluded, and why?
bands = ["Rush", "Yes", "Genesis"]
selected = {band: len(band) for band in bands if len(band) >= 4}
print(selected)
print(len(selected))
# ANSWER:
# {'Rush': 4, 'Genesis': 7}
# 2
# Which input names are excluded, and why?: Yes is excluded because the loop has an if condition
# that is checking the band variable lenth >= 4

# Exercise 3 — Count repeated characters
# Predict both outputs. Explain why the dictionary has fewer entries than
# the word has characters.
word = "level"
counts = {letter: word.count(letter) for letter in word}
print(counts)
print(len(counts))
# ANSWER:
# {'l': 2, 'e': 2, 'v': 1}
# 3
# Explain why the dictionary has fewer entries than the word has characters: because the count function
# is counting the number of letter that is being looped over in the comprehension
# For "level", the loop visits l, e, v, e, l. A dictionary can hold only one entry per
#  distinct key. Visiting e again replaces its existing value with 2; it does not create
#  another entry. That leaves three keys: 'l', 'e', and 'v'.


# Exercise 4 — Dynamic key vs. literal key
# Predict both outputs. Explain why these comprehensions produce different
# numbers of entries and why one value replaces another.
words = ["tea", "coffee"]
dynamic = {word: len(word) for word in words}
literal = {"word": len(word) for word in words}
print(dynamic)
print(literal)
# ANSWER:
# {"tea": 3, "coffee": 6}
# {'word': 6}
# Explain why these comprehensions produce different
# numbers of entries and why one value replaces another: Need help on this one to understand literal
# Both assignments use the same key, so 6 replaces 3, leaving {'word': 6}.
# The dynamic comprehension uses two different keys: That is why it retains two entries.


# Exercise 5 — Rewrite a loop
# Rewrite this loop as a dictionary comprehension with the same result.
# Predict the resulting dictionary and explain your filter.
numbers = [1, 2, 3, 4, 5]
squares = {}
for number in numbers:
    if number % 2 == 0:
        squares[number] = number ** 2
print(squares)
# ANSWER:
# {2: 4, 4: 16}
# 
numbers = [1, 2, 3, 4, 5]
squares = {number: number ** 2 for number in numbers if number % 2 == 0}
print(squares)
# {2: 4, 4: 16} same output as loop, the filter read loops over numbers list checking if it is even
# and then squaring the result


# Exercise 6 — Build your own song-title dictionary
# 1. Create a list named titles with four distinct song titles.
# 2. Use a dictionary comprehension to map each title to its character count.
# 3. Print the dictionary.
# 4. Create a second dictionary comprehension that includes only titles with
#    lengths greater than 10 characters. Spaces count as characters.
# 5. Print the filtered dictionary and the original titles list.
# 6. Explain your key expression, value expression, and filter condition.
# Write your code below:
titles = [
    "Bad Moon Rising",
    "Fortunate Son",
    "Have You Ever Seen the Rain?",
    "Mary",
]

title_character_count = {letter: letter.count(letter) for letter in titles}
print(title_character_count)
other_titles = {word: len(word) for word in titles if len(word) > 10 }
print(other_titles)
# Explain your key expression, value expression, and filter condition: lets discuss this

# Optional challenge — Count only repeated letters
# Work through this one together when you are ready.
# Define repeated_letter_counts(word). Assume word contains only lowercase
# English letters, or is an empty string.
# Use a dictionary comprehension and count() to return each letter occurring
# MORE than once, mapped to its total count in the original word.
def repeated_letter_counts(word):
    repeated_count = {letter: word.count(letter) for letter in word if word.count(letter) > 1}
    return repeated_count


print(repeated_letter_counts("banana")) # => {'a': 3, 'n': 2}
print(repeated_letter_counts("level")) # => {'l': 2, 'e': 2}
print(repeated_letter_counts("cat")) # => {}
print(repeated_letter_counts("")) # => {}
# Explain why repeated visits to a letter do not increase the dictionary's length.
# Write your code below:
# One final understanding check: when the loop visits "a" three times in "banana",
#  why does the dictionary still have only one "a" entry: because the dict key already
# exists and thus gets updated with a new value instead of duplicating it
