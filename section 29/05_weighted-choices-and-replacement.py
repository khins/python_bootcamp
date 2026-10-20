# ============================================================
# FILE: 05_weighted-choices-and-replacement.py
# TOPIC: Deep Dive — Weighted Selection with choices
# ============================================================
# LESSON OBJECTIVES
# 1. Use choices() for multiple draws with replacement.
# 2. Model unequal probabilities using relative weights.
# 3. Distinguish probabilities from guaranteed counts.
# 4. Compare choice(), choices(), and sample().
#
# Predict before running. Uncomment individual example calls.

import random
from collections import Counter


# ============================================================
# SECTION 1 — choices(): A LIST OF DRAWS WITH REPLACEMENT
# ============================================================
def example_choices():
    colors = ["red", "green", "blue"]
    picks = random.choices(colors, k=5)
    print(picks)
    print(len(picks)) # => 5
    print(random.choices(colors, k=1)) # A one-item list.


# example_choices()
# An entry can be picked repeatedly. k may exceed population size.
# choice(colors) returns an item; choices(colors, k=1) returns a list.
# EXERCISE 1 — COMPARE
# Which function fits five draws from three entries with repeats?
# ANSWER: ____________________________________________________


# ============================================================
# SECTION 2 — RELATIVE WEIGHTS
# ============================================================
def example_weighted_choices():
    rewards = ["common", "uncommon", "rare"]
    results = random.choices(rewards, weights=[70, 25, 5], k=10)
    print(results)


# example_weighted_choices()
# Each weight corresponds to the entry at the same position.
# Probability = entry's weight / sum of all weights.
# These probabilities are 70%, 25%, and 5% per draw.
# Weights need not total 100: [14, 5, 1] gives the same probabilities.
# EXERCISE 2 — CALCULATE
# For weights [2, 3, 5], what is the second item's probability? ___


# ============================================================
# SECTION 3 — PROBABILITIES DO NOT ENFORCE QUOTAS
# ============================================================
def example_observed_counts():
    rng = random.Random(42)
    labels = ["common", "uncommon", "rare"]
    draws = rng.choices(labels, weights=[70, 25, 5], k=1000)
    counts = Counter(draws)
    for label in labels:
        print(label, counts[label], counts[label] / len(draws))


# example_observed_counts()
# Counter counts occurrences; missing labels have a count of zero.
# Observed proportions can differ from specified probabilities.
# To require exactly seven A entries and three B entries, construct
# that list and shuffle it instead of making ten weighted draws.
# EXERCISE 3 — EXPLAIN
# Does a 5% chance ensure one rare result in 20 draws?
# ANSWER: ____________________________________________________


# ============================================================
# SECTION 4 — CUMULATIVE WEIGHTS
# ============================================================
def example_cumulative_weights():
    labels = ["common", "uncommon", "rare"]
    print(random.choices(labels, cum_weights=[70, 95, 100], k=5))


# example_cumulative_weights()
# Cumulative weights are running totals: 70, 70+25, 70+25+5.
# These are equivalent to weights=[70, 25, 5].
# Supply weights OR cum_weights, not both.
# EXERCISE 4 — CONVERT
# Convert weights [2, 3, 5] to cumulative weights: _______________


# ============================================================
# SECTION 5 — VALID INPUTS AND COMMON MISTAKES
# ============================================================
# For positive k, use a nonempty population sequence.
# Supply one finite, nonnegative weight per entry with a positive total.
# A zero weight excludes the corresponding entry.
# Use a nonnegative integer k. Do not rely on the function to detect
# every malformed weight sequence.
# Mismatched weight counts and all-zero weights raise ValueError.
# Supplying both weights and cum_weights raises TypeError.

def example_invalid_weights():
    try:
        random.choices(["a", "b"], weights=[0, 0], k=1)
    except ValueError:
        print("The total weight must be positive.")


# example_invalid_weights()
# With the same seed, repeated choice() calls and one choices() call
# need not yield identical sequences: their algorithms differ.


# ============================================================
# SECTION 6 — SELECT THE RIGHT OPERATION
# ============================================================
# choice(items)             One item, equal chance per entry.
# choices(items, k=n)       A list of n draws with replacement.
# choices(..., weights=...) Weighted draws with replacement.
# sample(items, k=n)        A list of n entries without replacement.
# shuffle(items)            Reorder a mutable sequence in place.
#
# sample() does not accept weights. Weighted sampling without
# replacement is a separate problem from choices().


# ============================================================
# SECTION 7 — CODING CHALLENGES
# ============================================================
# CHALLENGE 1: Simulate 100 support tickets with priorities
# "low", "medium", "high" weighted 6, 3, 1. Count each priority.
# Explain why counts need not be exactly 60, 30, and 10.
# Write your code here:


# CHALLENGE 2: Build exactly eight "regular" and two "VIP" tickets,
# then randomize their order. Compare with ten choices() draws
# using weights [8, 2]. Which guarantees the composition?
# Write your code here:


# ============================================================
# SECTION 8 — FINAL REVIEW
# ============================================================
# 1. Does choices() sample with replacement? __________________
# 2. What type does choices(..., k=1) return? __________________
# 3. Must relative weights sum to 100? _________________________
# 4. What does a zero weight mean? _____________________________
# 5. How do weights differ from cumulative weights? ____________
# 6. How would you enforce exact category counts? ______________
#
# KEY TAKEAWAY:
# choices() makes repeated, optionally weighted draws. Weights
# describe probabilities, not exact counts in the output.
# ============================================================
# END OF LESSON
# ============================================================
