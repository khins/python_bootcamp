# SECTION 8: CONTROL FLOW REVIEW
# Complete the function stubs below, replacing each pass with your code.
# Return results from your functions; use print only for checking your work.
# Assume inputs have the types and ranges stated in each assignment.
# Match the expected strings exactly, including capitalization and spaces.
# No imports are needed. Leave the examples as comments until ready to try them.
#
# QUICK REVIEW
# - if / elif / else chooses a branch; the first matching branch runs.
# - Check specific or overlapping conditions before broader conditions.
# - Comparisons produce booleans; and, or, and not combine or negate conditions.
# - The % operator gives a remainder and can check divisibility.
# - Empty strings, zero, and None are falsy; nonempty strings are truthy.
# - return ends the current function call immediately.
# - Recursion needs a base case and a step that moves toward it.
#
# GRADING: 100 points total (weights listed below).
# Each assignment is graded on its stated behavior, boundary cases, and any
# required technique. Examples are checks, not the only possible inputs.
# When ready, save this file and ask: "Grade my section 8 control flow review."


# 1. NUMBER SIGN -- 10 points
# Accept an integer. Return "positive", "negative", or "zero".
# Use if / elif / else.
# number_sign(8) => "positive"
# number_sign(-3) => "negative"
# number_sign(0) => "zero"
def number_sign(number):
    if number > 0:
        return "positive"
    elif number < 0:
        return "negative"
    else:
        return "zero"

print(number_sign(8))
print(number_sign(-3))
print(number_sign(0))


# 2. DISPLAY NAME -- 10 points
# Accept a string or None. If the value is truthy, return it unchanged.
# Otherwise, return "Guest". Use a truthiness check.
# A string containing only spaces still counts as truthy for this exercise.
# display_name("Kevin") => "Kevin"
# display_name("") => "Guest"
# display_name(None) => "Guest"
# display_name(" ") => " "
def display_name(name):
    if name == None:
        return "Guest"
    if name.isspace():
        return name
    if bool(name):
        return name
    elif bool(name) == False:
        return "Guest"

print(display_name("Kevin"))
print(display_name(""))
print(display_name(None))
print(display_name(" "))


# 3. LETTER GRADE -- 15 points
# Accept an integer score (including values outside 0 through 100).
# Return "Invalid" for scores below 0 or above 100.
# Otherwise return: 90-100: "A", 80-89: "B", 70-79: "C",
# 60-69: "D", 0-59: "F". Use conditional branches.
# letter_grade(-1) => "Invalid"
# letter_grade(0) => "F"
# letter_grade(59) => "F"
# letter_grade(60) => "D"
# letter_grade(70) => "C"
# letter_grade(80) => "B"
# letter_grade(89) => "B"
# letter_grade(90) => "A"
# letter_grade(100) => "A"
# letter_grade(101) => "Invalid"
def letter_grade(score):
    if score < 0:
        return "Invalid"

    if score < 60:
        return "F"
    elif score < 70:
        return "D"
    elif score < 80:
        return "C"
    elif score < 90:
        return "B"
    elif score <= 100:
        return "A"
    else:
        return "Invalid"

print(letter_grade(-1))
print(letter_grade(0))
print(letter_grade(59))
print(letter_grade(60))
print(letter_grade(70))
print(letter_grade(80))
print(letter_grade(89))
print(letter_grade(90))
print(letter_grade(100))
print(letter_grade(101))

# 4. ENTRY PERMISSION -- 15 points
# Accept a nonnegative integer age and two booleans.
# Return True only if the person is NOT banned AND either:
# - they are at least 18, OR
# - they have guardian permission.
# Otherwise return False. Use and, or, and not in your solution.
# can_enter(18, False, False) => True
# can_enter(17, False, False) => False
# can_enter(17, True, False) => True
# can_enter(25, True, True) => False
# can_enter(12, True, True) => False
def can_enter(age, has_guardian_permission, is_banned):
    if is_banned == True:
        return False
    if age >= 18:
        return True
    elif age < 18 and has_guardian_permission == True:
        return True
    else: 
        return False

print("-" * 10)

print(can_enter(18, False, False))
print(can_enter(17, False, False))
print(can_enter(17, True, False))
print(can_enter(25, True, True))
print(can_enter(12, True, True))

print("-" * 10)

# 5. ABSOLUTE DIFFERENCE -- 10 points
# Accept two integers and return their nonnegative difference.
# Use a conditional. Do not use abs(), min(), or max().
# absolute_difference(9, 4) => 5
# absolute_difference(4, 9) => 5
# absolute_difference(6, 6) => 0
# absolute_difference(-3, 2) => 5
def absolute_difference(first, second):
    if first >= second:
        return first - second
    else:
        return second - first

print(absolute_difference(9, 4))
print(absolute_difference(4, 9))
print(absolute_difference(6, 6))
print(absolute_difference(-3, 2))


# 6. DIVISIBILITY LABEL -- 15 points
# Accept a positive integer.
# Return "TwoSeven" if divisible by both 2 and 7, "Two" if only by 2,
# "Seven" if only by 7, or the original integer if divisible by neither.
# Use modulo and conditional branches.
# divisibility_label(14) => "TwoSeven"
# divisibility_label(4) => "Two"
# divisibility_label(21) => "Seven"
# divisibility_label(9) => 9
# divisibility_label(28) => "TwoSeven"
def divisibility_label(number):
    if number % 2 == 0 and number % 7 == 0:
        return "TwoSeven"
    elif number % 2 == 0:
        return "Two"
    elif number % 7 == 0:
        return "Seven"
    else:
        return number

print(divisibility_label(14))
print(divisibility_label(4))
print(divisibility_label(21))
print(divisibility_label(9))
print(divisibility_label(28))


# 7. RECURSIVE SUM -- 15 points
# Accept an integer from 0 through 100.
# Return the sum of all integers from 1 through number; return 0 for input 0.
# Your function MUST call itself. Do not use loops or sum().
# recursive_sum(0) => 0
# recursive_sum(1) => 1
# recursive_sum(2) => 3
# recursive_sum(5) => 15
# recursive_sum(10) => 55
def recursive_sum(number):
    if number == 0:
        return 0

    return number + recursive_sum(number - 1)

print(recursive_sum(0))
print(recursive_sum(1))
print(recursive_sum(2))
print(recursive_sum(5))
print(recursive_sum(10))

# 8. EXPLAIN THE FLOW -- 10 points (5 points per answer)
# Write your answers in comments. You do not need to change the sample code.
# A. What does mystery(15) return, and why doesn't its second branch run?
# def mystery(number):
#     if number % 3 == 0:
#         return "Three"
#     elif number % 3 == 0 and number % 5 == 0:
#         return "Both"
#     return number
# ANSWER A:
# The answer will be Three because it is the first evaulation and it is a truthy statement 
# therefore no need to continue through to the second branch

#
# B. In recursive_sum, what is your base case, and how does each recursive
# call move toward it? What would happen if there were no stopping condition?
# ANSWER B:
# The base case is 0 and the recursive call moves toward it by subtracting 1 each time it 
# calls the same function again. If there was no stopping condition eventually there would
# be an out of memory exception.


# SCRATCH SPACE: Add print calls below to check your completed functions.
# Example:
# print(number_sign(-3))  # Expected: "negative"

# Updated grade: 86/90 (95.6%)
# mostly correct on # 8- B the error is a RecursionError
