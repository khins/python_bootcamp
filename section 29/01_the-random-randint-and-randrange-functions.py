# ============================================================
# FILE: 01_the-random-randint-and-randrange-functions.py
# TOPIC: Random Numbers and Integer Ranges
# ============================================================
# LESSON OBJECTIVES
# 1. Generate pseudorandom floats and integers.
# 2. Distinguish inclusive and exclusive endpoints.
# 3. Select integers using a step.
# 4. Model a probability with a threshold.
#
# Predict before running. Uncomment individual example calls.
# Random output varies; comments describe possible results.

import random


# ============================================================
# SECTION 1 — WHAT DOES PSEUDORANDOM MEAN?
# ============================================================
# random uses an algorithm with internal state to generate values.
# Use it for games, practice programs, and simulations.
# It is not suitable for passwords or security tokens; use the
# secrets module for security-sensitive randomness.
# Random draws can repeat and need not look balanced in small samples.


# ============================================================
# SECTION 2 — random(): A FLOAT IN [0.0, 1.0)
# ============================================================
def example_random_float():
    value = random.random()
    print(value)
    print(0.0 <= value < 1.0)  # => True


# example_random_float()
# 0.0 is included; 1.0 is excluded. The result is a float.
# EXERCISE 1 — PREDICT
# Could the result be 0.25? ________ Exactly 1.0? ________
# Could it be negative? ________


# ============================================================
# SECTION 3 — randint(): BOTH ENDPOINTS INCLUDED
# ============================================================
def example_dice():
    for _ in range(5):
        print(random.randint(1, 6))  # An integer from 1 through 6.


# example_dice()
# randint(a, b) includes both a and b. Repeated rolls may match.
# randint(4, 4) always returns 4.
# EXERCISE 2 — COUNT
# How many possible results does randint(10, 15) have? __________
# Smallest result? __________ Largest result? __________


# ============================================================
# SECTION 4 — randrange(): SELECT FROM A range
# ============================================================
def example_ranges():
    print(random.randrange(5))         # 0, 1, 2, 3, or 4.
    print(random.randrange(2, 6))      # 2, 3, 4, or 5.
    print(random.randrange(2, 11, 2))  # 2, 4, 6, 8, or 10.
    print(random.randrange(10, 0, -2)) # 10, 8, 6, 4, or 2.


# example_ranges()
# Forms: randrange(stop), randrange(start, stop), or
# randrange(start, stop, step). The stop value is always excluded.
# randint(a, b) has the same possible results as randrange(a, b + 1).
# EXERCISE 3 — LIST ALL POSSIBLE RESULTS
# random.randrange(3, 16, 4)
# ANSWER: ____________________________________________________


# ============================================================
# SECTION 5 — INVALID RANGES
# ============================================================
def example_invalid_range():
    try:
        print(random.randrange(5, 5))
    except ValueError:
        print("There are no values to choose from.")


# example_invalid_range()
# Use integer arguments. An empty range or zero step raises ValueError.
# Keep these intentional errors commented out:
# random.randint(6, 1)
# random.randrange(1, 10, 0)
# EXERCISE 4 — EXPLAIN
# Why does randint(5, 5) work but randrange(5, 5) fail?
# ANSWER: ____________________________________________________


# ============================================================
# SECTION 6 — MODEL A CHANCE WITH A THRESHOLD
# ============================================================
def example_probability():
    if random.random() < 0.25:
        print("Bonus awarded!")
    else:
        print("No bonus this time.")


# example_probability()
# This models approximately a 25% chance per trial, not a guarantee
# of exactly one success in every four trials.
# EXERCISE 5 — MODIFY
# Which threshold would model a 70% chance? ____________________


# ============================================================
# SECTION 7 — CODING CHALLENGES
# ============================================================
# CHALLENGE 1: Write roll_two_dice(). Return the sum of two separate
# randint(1, 6) draws. Identify the minimum and maximum possible sum.
# Is this the same distribution as randint(2, 12)? Explain.
# Write your code here:


# CHALLENGE 2: Print ten random multiples of 5 from 5 through 50.
# Use randrange() inside a loop. Repeated values are allowed.
# Write your code here:


# ============================================================
# SECTION 8 — FINAL REVIEW
# ============================================================
# 1. Which function returns a float in [0.0, 1.0)? _______________
# 2. Which integer function includes both endpoints? ___________
# 3. Is stop included in randrange()? __________________________
# 4. What does the third randrange argument control? ___________
# 5. Can independent random draws repeat? _____________________
# 6. Does a 25% chance guarantee one success in four tries? _____
#
# KEY TAKEAWAY:
# Use random() for thresholds, randint() for inclusive integer
# bounds, and randrange() for selections from a range.
# ============================================================
# END OF LESSON
# ============================================================
