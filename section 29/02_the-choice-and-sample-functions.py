# ============================================================
# FILE: 02_the-choice-and-sample-functions.py
# TOPIC: Selecting Items with choice and sample
# ============================================================
# LESSON OBJECTIVES
# 1. Select one item with choice().
# 2. Select multiple entries without replacement using sample().
# 3. Understand sizes, return types, and duplicate values.
# 4. Keep the original sequence unchanged.
#
# Predict before running. Uncomment individual example calls.

import random


# ============================================================
# SECTION 1 — choice(): ONE ITEM FROM A SEQUENCE
# ============================================================
def example_choice():
    albums = ["Blue", "Kind of Blue", "Abbey Road"]
    selected = random.choice(albums)
    print(selected)            # One title, a string.
    print(selected in albums)  # => True
    print(albums)              # Original list is unchanged.


# example_choice()
# choice() returns an item, not a one-item list.
# Lists, tuples, strings, and range objects are valid sequences.
# choice("Python") returns one character.
# EXERCISE 1 — PREDICT THE TYPE
# choice([10, 20, 30]): ________ choice("abc"): ________


# ============================================================
# SECTION 2 — REPEATED choice CALLS CAN REPEAT ENTRIES
# ============================================================
def example_repeated_choices():
    colors = ["red", "green", "blue"]
    picks = [random.choice(colors) for _ in range(5)]
    print(picks)
    print(len(picks))  # => 5


# example_repeated_choices()
# Each call selects from the full sequence. No entry is removed.
# This is sampling WITH replacement.
# EXERCISE 2 — EXPLAIN
# Why can five picks be made from only three colors?
# ANSWER: ____________________________________________________


# ============================================================
# SECTION 3 — sample(): ENTRIES WITHOUT REPLACEMENT
# ============================================================
def example_sample():
    players = ["Ada", "Grace", "Linus", "Guido"]
    team = random.sample(players, k=2)
    print(team)         # A new list containing two selected players.
    print(len(team))    # => 2
    print(players)      # Original order and contents are unchanged.


# example_sample()
# Each entry can be selected at most once within one sample.
# The result is always a new list, even for a tuple or string input.
# Its order is selection order, not necessarily source order.
# EXERCISE 3 — COMPARE
# How do choice(players) and sample(players, k=1) differ?
# ANSWER: ____________________________________________________


# ============================================================
# SECTION 4 — UNIQUE ENTRIES VERSUS UNIQUE VALUES
# ============================================================
def example_duplicate_values():
    tickets = ["Ada", "Ada", "Grace"]
    print(random.sample(tickets, k=3)) # Two Ada values and one Grace.


# example_duplicate_values()
# Each position is a separate entry. Duplicate input values can
# therefore appear together in one sample.
# choice(tickets) also favors Ada: two of the three entries say Ada.
# EXERCISE 4 — EXPLAIN
# If each person may win only once, how should the population be built?
# ANSWER: ____________________________________________________


# ============================================================
# SECTION 5 — SIZES AND INPUT REQUIREMENTS
# ============================================================
def example_sample_sizes():
    numbers = [10, 20, 30]
    print(random.sample(numbers, k=0)) # => []
    print(random.sample(numbers, k=3)) # All entries in random order.
    try:
        random.sample(numbers, k=4)
    except ValueError:
        print("The requested sample is too large.")


# example_sample_sizes()
# For these ordinary samples, k is an integer from 0 to len(source).
# Negative k also raises ValueError. choice([]) raises IndexError.
# Use a sequence, not a set, dictionary, or generator directly.
# To choose dictionary keys, first convert them to a list:
# selected = random.choice(list({"a": 10, "b": 20}))
# sorted(my_set) gives a stable sequence if the set's values are comparable.


# ============================================================
# SECTION 6 — SAMPLE FROM A RANGE
# ============================================================
def example_unique_numbers():
    numbers = random.sample(range(1, 50), k=6)
    print(numbers)          # Six distinct integers from 1 through 49.
    print(sorted(numbers))  # A sorted copy for easier reading.


# example_unique_numbers()
# A range avoids building a list of every candidate integer.
# EXERCISE 5 — MODIFY
# How would you include 50 as a possible result? ________________


# ============================================================
# SECTION 7 — CODING CHALLENGES
# ============================================================
# CHALLENGE 1: Write pick_album(albums). Return one random title,
# or None when the sequence is empty. Test zero, one, and many titles.
# Write your code here:


# CHALLENGE 2: Select three questions from eight unique question
# strings. Print them numbered from 1 to 3. Preserve the source list.
# Write your code here:


# ============================================================
# SECTION 8 — FINAL REVIEW
# ============================================================
# 1. Does choice() remove the chosen entry? ____________________
# 2. What type does sample() return? ___________________________
# 3. What does without replacement mean? ______________________
# 4. Can duplicate input values appear in one sample? __________
# 5. What happens when k exceeds the population size? __________
# 6. What does sample(items, k=0) return? ______________________
#
# KEY TAKEAWAY:
# choice() selects one item. sample() returns a new list of entries
# selected without replacement, leaving the source unchanged.
# ============================================================
# END OF LESSON
# ============================================================
