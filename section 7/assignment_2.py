# Section 7 - Assignment 2: String Methods Review
# Complete each function below. Replace pass with your solution.
# Suggested methods: find(), count(), lower(), strip(), replace(), endswith().
# Uncomment the example calls as you complete each exercise.


# 1. Define first_position(text, target).
# Return the first index of target in text, or -1 if it is absent.
# Method to review: find()
# EXAMPLES:
# first_position("banana", "a") => 1
# first_position("banana", "z") => -1
def first_position(text, target):
    return text.find(target)

print(first_position("banana", "a"))
print(first_position("banana", "z"))


# 2. Define count_letter(text, letter).
# Return how many times letter appears. Assume letter is one character.
# Matching should be case-sensitive.
# Method to review: count()
# EXAMPLES:
# count_letter("banana", "a") => 3
# count_letter("Apple", "a") => 0
def count_letter(text, letter):
    return text.count(letter)



print(count_letter("banana", "a"))
print(count_letter("Apple", "a"))


# 3. Define make_lowercase(text).
# Return a lowercase version of text.
# Method to review: lower()
# EXAMPLES:
# make_lowercase("Hello PYTHON!") => "hello python!"
# make_lowercase("123") => "123"
def make_lowercase(text):
    return text.lower()


print(make_lowercase("Hello PYTHON!"))
print(make_lowercase("123"))


# 4. Define clean_edges(text).
# Remove whitespace from the beginning and end, keeping spaces inside.
# Method to review: strip()
# EXAMPLES:
# clean_edges("  hello world  ") => "hello world"
# clean_edges("   ") => ""
def clean_edges(text):
    return text.rstrip().lstrip()


print(repr(clean_edges("  hello world  ")))
print(repr(clean_edges("   ")))
# repr() makes spaces and empty strings easier to see in printed output.


# 5. Define replace_spaces(text).
# Return text with every space replaced by a hyphen.
# Method to review: replace()
# EXAMPLES:
# replace_spaces("learning Python is fun") => "learning-Python-is-fun"
# replace_spaces("hello") => "hello"
def replace_spaces(text):
    return text.replace(" ", "-")


print(replace_spaces("learning Python is fun"))
print(replace_spaces("hello"))


# 6. Define is_python_file(filename).
# Return True if filename ends with ".py", otherwise False.
# Matching should be case-sensitive.
# Method to review: endswith()
# EXAMPLES:
# is_python_file("assignment.py") => True
# is_python_file("assignment.py.txt") => False
# is_python_file("assignment.PY") => False
def is_python_file(filename):
    return filename.endswith(".py")

print(is_python_file("assignment.py"))
print(is_python_file("assignment.py.txt"))
print(is_python_file("assignment.PY"))


# 7. Challenge: Define normalize_name(text).
# Remove surrounding whitespace and convert the result to lowercase.
# Hint: Use two of the methods above. You can save an intermediate result.
# EXAMPLES:
# normalize_name("  KEVIN  ") => "kevin"
# normalize_name(" Mary Jane ") => "mary jane"
def normalize_name(text):
    return text.strip().lower()


print(normalize_name("  KEVIN  "))
print(normalize_name(" Mary Jane "))


# Research reflection:
# Pick one method that is new to you and answer these questions in comments:
#   endswith() method
# - What does it do?
#        endswith() accepts a suffix to check and returns True if the string ends
#        with that suffix; otherwise, it returns False. It leaves the original 
#       string unchanged.
# - What arguments does it accept, and what does it return?
#       it takes a string
# - Does it change the original string?
#       it does not change the original
# - What is one situation where you would use it?
#       when determining if a bunch of files in a folder contain a certain file type
# Write one additional example of your own.
def find_python_files(filename):
    return filename.endswith(".py")

print(find_python_files("test.py"))
print(find_python_files("example.xlsx"))

# Grade: 9/10. All seven functions produce the requested results.
