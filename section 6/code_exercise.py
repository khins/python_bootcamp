# Coding Exercise SOLUTION: String Indexing
# Define a same_first_and_last_letter function that accepts a string as an argument.
# The function should return a True if the first and last character are equal,
# and False otherwise
# Assume the string will always have 1 or more characters.
#
# EXAMPLES:
# same_first_and_last_letter("runner")    => True
# same_first_and_last_letter("Runner")    => False
# same_first_and_last_letter("clock")     => False
# same_first_and_last_letter("q")         => True
def same_first_and_last_letter(word):
    return word[0] == word[-1]

print(same_first_and_last_letter("runner"))
print(same_first_and_last_letter("Runner"))
print(same_first_and_last_letter("clock"))
print(same_first_and_last_letter("q") )


# Define a three_number_sum function that accepts a 3-character string as an argument.
# The function should add up the sum of the digits of the string.
# HINT: You'll have to figure out a way to convert the string-ified numbers to integers.
#
# EXAMPLES:
# three_number_sum("123")    => 6
# three_number_sum("567")    => 18
# three_number_sum("444")    => 12
# three_number_sum("000")    => 0
def three_number_sum(val):
    return int(val[0]) + int(val[1]) + int(val[2])

print(three_number_sum("123"))
print(three_number_sum("567"))
print(three_number_sum("444"))
print(three_number_sum("000"))
