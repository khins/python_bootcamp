# Section 11 - Debugging Practice
#
# The goal of this file is not to write brand-new solutions from scratch.
# Each function below already has code, but each one contains at least one bug.
#
# Practice the debugging flow:
# 1. Run this file.
# 2. Read the first failing check.
# 3. Add print statements or use the debugger to inspect the values.
# 4. Fix one function at a time.
# 5. Run the file again until every check passes.
#
# Avoid changing the check() or run_checks() functions until you have fixed the
# exercises. The bugs are inside the numbered exercise functions.


# Exercise 1
# Return the largest number from the list.
# The list will always contain at least one number.
def largest_number(numbers):
    largest = numbers[0] # when handling negatives start with the first element rather than zero

    for number in numbers:
        if number > largest:
            largest = number

    return largest

# print(largest_number([-10, -3, -25]))


# Exercise 2
# Count how many words have more than 5 characters.
def count_long_words(words):
    count = 0

    for word in words:
        if len(word) > 5:
            count += 1

    return count

# Exercise 3
# Return True if every number in the list is even.
# Return False if at least one number is odd.
def all_even(numbers):
    for number in numbers:
        if number % 2 != 0:
            return False

    return True


# Exercise 4
# Return the total price after applying a percentage discount.
# A 20 percent discount on 100 should return 80.0.
def discounted_price(price, discount_percent):
    discount = price * (discount_percent / 100)
    return price - discount


# Exercise 5
# Return a new list containing each word in uppercase.
def uppercase_words(words):
    updated_words = []

    for index in range(len(words)):
        updated_words.append(words[index].upper())

    return updated_words


# Exercise 6
# Return the index of the first word that starts with the target letter.
# Return -1 if no word starts with the target letter.
def first_word_starting_with(words, letter):
    for index, word in enumerate(words):
        if word[0] == letter:
            return index

    return -1


# Exercise 7
# Return a dictionary where each word maps to its length.
def word_lengths(words):
    lengths = {}

    for word in words:
        key = word
        lengths[key] = (len(word))

    return lengths


# Exercise 8
# Return the sum of all numbers from 1 through the provided number.
# For example, sum_to_number(4) should return 10 because 1 + 2 + 3 + 4 = 10.
def sum_to_number(number):
    total = 0

    for current_number in range(1, number + 1):
        total += current_number

    return total


def check(description, actual, expected):
    if actual == expected:
        print(f"PASS: {description}")
    else:
        print(f"FAIL: {description}")
        print(f"  Expected: {expected}")
        print(f"  Actual:   {actual}")


def run_checks():
    print("Section 11 Debugging Checks")
    print("---------------------------")

    check("largest_number handles positive numbers", largest_number([3, 8, 2]), 8)
    check("largest_number handles negative numbers", largest_number([-10, -3, -25]), -3)

    check("count_long_words ignores 5-letter words", count_long_words(["apple", "python", "code"]), 1)
    check("count_long_words counts longer words", count_long_words(["debugging", "loops", "variable"]), 2)

    check("all_even returns True for all even numbers", all_even([2, 4, 6]), True)
    check("all_even returns False when one number is odd", all_even([2, 3, 4]), False)

    check("discounted_price applies 20 percent discount", discounted_price(100, 20), 80.0)
    check("discounted_price applies 15 percent discount", discounted_price(80, 15), 68.0)

    original_words = ["hello", "world"]
    check("uppercase_words returns uppercase values", uppercase_words(original_words), ["HELLO", "WORLD"])
    check("uppercase_words does not mutate the original list", original_words, ["hello", "world"])

    check("first_word_starting_with finds a matching index", first_word_starting_with(["cat", "dog", "duck"], "d"), 1)
    check("first_word_starting_with returns -1 without a match", first_word_starting_with(["cat", "dog"], "z"), -1)

    check("word_lengths tracks every word", word_lengths(["red", "green", "blue"]), {"red": 3, "green": 5, "blue": 4})
    check("word_lengths handles an empty list", word_lengths([]), {})

    check("sum_to_number includes the final number", sum_to_number(4), 10)
    check("sum_to_number works for 1", sum_to_number(1), 1)


run_checks()
