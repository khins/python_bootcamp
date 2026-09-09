# Define a even_or_odd function that accepts a single integer.
# If the integer is even, the function should return the string "even".
# If the integer is odd, the function should return the string "odd".
#
# even_or_odd(2)    => "even"
# even_or_odd(0)    => "even"
# even_or_odd(13)   => "odd"
# even_or_odd(9)    => "odd"
def even_or_odd(num):
    if num % 2 == 0:
        return "even"
    else:
        return "odd"

print(even_or_odd(2))
print(even_or_odd(0))
print(even_or_odd(13))
print(even_or_odd(9))



# Define a truthy_or_falsy function that accepts a single argument.
# The function should return a string that reads "The value _____ is _____"
# where the first space is the argument and the second space
# is either 'truthy' or 'falsy'. See the sample invocations below.
#
# truthy_or_falsy(0)        => "The value 0 is falsy"
# truthy_or_falsy(5)        => "The value 5 is truthy"
# truthy_or_falsy("Hello")  => "The value Hello is truthy"
# truthy_or_falsy("")       => "The value  is falsy"
# truthy_or_falsy("")       => "The value  is falsy"
def truthy_or_falsy(num):
    if bool(num):
        return f'The value of {num} is truthy'
    else:
        return f'The value of {num} is falsy'

print(truthy_or_falsy(0))
print(truthy_or_falsy(5))
print(truthy_or_falsy("Hello"))
print(truthy_or_falsy(""))

# Declare a negative_energy function that accepts a numeric argument
# and returns its absolute value.
# The absolute value is the number's distance from zero.
#
# negative_energy(5)    => 5
# negative_energy(10)   => 10
# negative_energy(-5)   => 5
# negative_energy(-8)   => 8
# negative_energy(0)    => 0
def negative_energy(num):
    return abs(num)

print(negative_energy(5))
print(negative_energy(10))
print(negative_energy(-5))
print(negative_energy(-8))
print(negative_energy(0))

# Define a divisible_by_three_and_four function that accepts a number as its argument.
# It should return True if the number is evenly divisible by both 3 and 4.
# It should return False otherwise.
#
# divisible_by_three_and_four(3)   => False
# divisible_by_three_and_four(4)   => False
# divisible_by_three_and_four(12)  => True
# divisible_by_three_and_four(18)  => False
# divisible_by_three_and_four(24)  => True
def divisible_by_three_and_four(num):
    if num % 3 == 0 and num % 4 == 0:     
        return True 
    else:
        return False

print(divisible_by_three_and_four(3))
print(divisible_by_three_and_four(4))
print(divisible_by_three_and_four(12))
print(divisible_by_three_and_four(18))
print(divisible_by_three_and_four(24))
    


# Declare a string_theory function that accepts a string as an argument.
# It should return True if the string has more than 3 characters
# and starts with a capital "S". It should return False otherwise.
#
# string_theory("Sansa")  => True
# string_theory("Story")  => True
# string_theory("See")    => False
# string_theory("Fable")  => False
def string_theory(string):
    if string.startswith("S") and len(string) > 3:
        return True
    else:
        return False

print(string_theory("Sansa"))
print(string_theory("Story"))
print(string_theory("See"))
print(string_theory("Fable"))