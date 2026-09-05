# Define a easy_money function that accepts no parameters 
# and always returns the value 100.
def easy_money():
    return 100


# Define a best_food_ever function that accepts 
# no parameters and always returns the string “Sushi”.
def best_food_ever():
    return "Sushi"



# Define a convert_to_currency function that accepts a single parameter (an integer). 
# The function should convert the argument to a string, prefix it with a dollar sign, and return the result.
# 
# EXAMPLES:
# convert_to_currency(15)    => "$15"
# convert_to_currency(8)     => "$8"

def convert_to_currency(a):
    return '$' + str(a)

# 1 Return a fixed value
def favorite_place():
    return 'The Missouri Ozarks'

print(favorite_place())

# 2 Double a number
def double_number(number):
    return number * 2

print(double_number(7))

# 3 Create a greeting
def greet_person(name):
    return f'Hello, {name}!'

print(greet_person("Bob"))

# 4 Add two numbers
def add_numbers(first, second):
    return first + second

print(add_numbers(7,9))
print(add_numbers(57,91))

# Build a price label 
def price_label(item, price):
    
    return f'{item} costs {convert_to_currency(price)}'

print(price_label("Notebook", 11))