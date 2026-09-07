# Define a first_three_characters function that accepts a string argument.
# The function should return the first 3 characters of the string.
#
# EXAMPLES:
# first_three_characters("dynasty") => "dyn"
# first_three_characters("empire")  => "emp"
def first_three_characters(string):
    return string[0:3]

print(first_three_characters("dynasty"))
print(first_three_characters("empire"))


# Define a last_five_characters function that accepts a string argument.
# The function should return the last 5 characters of the string.
#
# EXAMPLES:
# last_five_characters("dynasty") => "nasty"
# last_five_characters("empire")  => "mpire"
def last_five_characters(string):
    return string[-5:]

print(last_five_characters("dynasty"))
print(last_five_characters("empire"))

# Define a is_palindrome function that accepts a string argument.
# The function should return True if the string is spelled
# the same backwards as it is forwards.
# Return False otherwise.
#
# EXAMPLES:
# is_palindrome("racecar") => True
# is_palindrome("yummy")   => False
def is_palindrome(string):
    return string == string[::-1]

print(is_palindrome("racecar"))
print(is_palindrome("yummy"))

# 1 Remove the ends
def remove_ends(text): 
    return text[1:-1]

print(remove_ends("Python"))
print(remove_ends("hi"))

# 2 Every other character
def every_other(text):
    return text[0::2]

print(every_other("abcdefg"))
print(every_other("Python"))

# 3 The other alternating characters
def alternate_from_second(text):
    return text[1::2]

print(alternate_from_second("abcdefg"))

#4 First half
def first_half(text):
    text_start = len(text) // 2
    return text[text_start::]

print(first_half("Python!"))
print(first_half("abcde"))

# 5 Middle three
def middle_three(text):
    mid_index = len(text) // 2
    return text[(mid_index-1):mid_index+2]

print(middle_three("Python!"))
print(middle_three("abcde"))

# 6 Rotate left
def rotate_left(text, n):
    first = text[:n]
    last = text[n:]
    
    return last + first


print(rotate_left("Python", 2))

# 7 Reverse a section
def reverse_section(text, start, stop):
    before = text[:start]
    mid = text[start:stop]
    after = text[stop:]
    reversed_mid = mid[::-1]
    return before + reversed_mid + after


print(reverse_section("abcdefg", 2, 5))
