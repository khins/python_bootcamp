# FizzBuzz coding session
# Define a fizzbuzz function that accepts a single integer.
# Return "FizzBuzz" if the number is evenly divisible by both 3 and 5.
# Return "Fizz" if the number is evenly divisible by 3 only.
# Return "Buzz" if the number is evenly divisible by 5 only.
# Otherwise, return the original number.
#
# Examples:
# fizzbuzz(3)   => "Fizz"
# fizzbuzz(5)   => "Buzz"
# fizzbuzz(15)  => "FizzBuzz"
# fizzbuzz(7)   => 7


def fizzbuzz(number):
    if (number % 3 == 0 and number % 5 == 0):
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return number


# Uncomment these calls as you work through the tutorial.
print(fizzbuzz(3))
print(fizzbuzz(5))
print(fizzbuzz(15))
print(fizzbuzz(7))

# Grade: 100% — all four requirements are correct.
# Optional practice: Print the FizzBuzz result for each number from 1 to 100.
