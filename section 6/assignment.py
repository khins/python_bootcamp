# Define a long_word function that accepts a string.
# The function should return a Boolean that reflects
# whether the string has more than 7 characters.
#
# EXAMPLES:
# long_word("Python")          => False
# long_word("magnificent")     => True
def long_word(val):
    return len(val) > 7

print(long_word("Python"))
print(long_word("magnificent"))

# Define a first_longer_than_second function that accepts two string arguments.
# The function should return a True if the first string is longer than the second
# and False otherwise (including if they are equal in length).
#
# EXAMPLES:
# first_longer_than_second("Python", "Ruby")       => True
# first_longer_than_second("cat", "mouse")         => False
# first_longer_than_second("Steven", "Seagal")     => False
def first_longer_than_second(val1,val2):
    return len(val1) > len(val2)

print(first_longer_than_second("Python", "Ruby"))
print(first_longer_than_second("cat", "mouse"))
print(first_longer_than_second("Steven", "Seagal"))

# 1 First character
def first_character(text):
    return text[0]

print(first_character("Python"))

# 2 Last character 
def last_character(text):
    return text[-1]

print(last_character("Python"))

# 3 Choose a position
def character_at(text, position):
    return text[position]

print(character_at("Python", 2))

# 4 Matching ends
def matching_ends(text):
    return text[0] == text[-1]

print(matching_ends("radar"))
print(matching_ends("python"))

# 5 Middle character
def middle_character(text):
    text_len = len(text)
    mid = text_len // 2
    return text[mid]

print(middle_character("cat"))
print(middle_character("Python!"))

# Grade: 5/5 — all string indexing tasks are correct!