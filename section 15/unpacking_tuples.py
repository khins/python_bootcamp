# Python Tuple Unpacking with * — Study Summary

# This lesson expands tuple unpacking by introducing the asterisk * syntax,
# which allows one variable to collect multiple values into a list.
employee = ("Bob", "Johnson", "Manager", 50)
first_name, last_name, position, age = employee

# Using * to capture remaining values
first_name, last_name, *details = employee

print(first_name)  # Bob
print(last_name)   # Johnson
print(details)     # ["Manager", 50]

# Python assigns "Bob" and "Johnson" normally, then *details collects
# everything remaining. Importantly, the collected values are stored
# in a list, not a tuple.
# Only one starred variable is allowed

# During a single unpacking operation, only one variable can use *.
# Key concept to remember

# The basic pattern is:

# first, *rest = values
# The biggest takeaway is that * gives tuple unpacking flexibility
# when you don't want or don't know exactly how many values one
# variable needs to capture, and those captured values are placed
# into a list.
first, last, *details = employee

# Given the tuple below, destructure the three values and
# assign them to position, city and salary variables
# Do NOT use index positions (i.e. job_opening[1])
job_opening = ("Software Engineer", "New York City", 100000)
position, city, salary = job_opening

# Given the tuple below,
# - destructure the first value and assign it to a street variable
# - destructure the last value and assign it to a zip_code variable
# - destructure the middle two values into a list and assign it to a city_and_state variable
address = ("35 Elm Street", "San Francisco", "CA", "94107")
street, city, state, zip_code = address
print(f'Full address is {street} {city} {state} {zip_code}')

# Declare a sum_of_evens_and_odds function that accepts a tuple of numbers.
# It should return a tuple with two numeric values:
# -- the sum of the even numbers
# -- the sum of the odd numbers.
def sum_of_evens_and_odds(numbers):

    # This is one version to solve there is another more pythonic version
    # for numb in numbers:
    #     if numb % 2 == 0:
    #         even_total += numb
    #     else:
    #         odd_total += numb

    # return (even_total, odd_total)
    # 
    # Pythonic verison
    even_total = [numb for numb in numbers if numb % 2 == 0]
    odd_total = [numb for numb in numbers if numb % 2 != 0]
    return sum(even_total), sum(odd_total)

print(sum_of_evens_and_odds((1, 2, 3, 4)))   #=> (6, 4)
print(sum_of_evens_and_odds((1, 3, 5)))    #=> (0, 9)
print(sum_of_evens_and_odds((2, 4, 6)))      #=> (12, 0)