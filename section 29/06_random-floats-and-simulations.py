# ============================================================
# FILE: 06_random-floats-and-simulations.py
# TOPIC: Deep Dive — Random Floats and Simulations
# ============================================================
# LESSON OBJECTIVES
# 1. Generate floating-point values using uniform().
# 2. Distinguish uniform and Gaussian distributions.
# 3. Summarize repeated trials.
# 4. Recognize the limits of a random simulation.
#
# Predict before running. Uncomment individual example calls.

import random
from collections import Counter


# ============================================================
# SECTION 1 — uniform(): FLOATS BETWEEN TWO BOUNDS
# ============================================================
def example_uniform():
    temperature = random.uniform(18.0, 24.0)
    print(temperature)
    print(f"{temperature:.1f}") # Display with one decimal place.


# example_uniform()
# The upper endpoint may or may not occur due to floating-point rounding.
# uniform() does not use an integer step, unlike randrange().
# Formatting changes the display, not the stored value.
# EXERCISE 1 — CHOOSE
# For a measurement with fractions, would you use randint or uniform?
# ANSWER: ____________________________________________________


# ============================================================
# SECTION 2 — DECIMAL VALUES VERSUS DISCRETE INCREMENTS
# ============================================================
def example_discrete_amount():
    cents = random.randint(100, 500)
    print(cents)                # Integer cents from 100 through 500.
    print(f"${cents / 100:.2f}") # Display from $1.00 to $5.00.


# example_discrete_amount()
# For equally likely cent amounts, draw integer cents directly.
# Rounding uniform(1, 5) to two decimal places does not give every
# cent amount equal probability, especially at the endpoints.
# Keep integer cents for arithmetic when exact cent amounts matter.
# EXERCISE 2 — MODIFY
# Which randrange arguments produce 200 through 1000 cents in
# 25-cent increments?
# ANSWER: ____________________________________________________


# ============================================================
# SECTION 3 — gauss(): VALUES CLUSTERED AROUND A MEAN
# ============================================================
def example_gaussian():
    for _ in range(5):
        print(random.gauss(mu=100, sigma=15))


# example_gaussian()
# mu is the mean; sigma is the standard deviation. Use positive sigma.
# Intervals near the mean are more likely than equally sized intervals
# far from the mean. A Gaussian has no fixed lower or upper bound.
# gauss(100, 15) does not guarantee results between 85 and 115.
# Negative values can occur even when the mean is positive.
# EXERCISE 3 — EXPLAIN
# Does gauss() alone enforce scores between 0 and 100?
# ANSWER: ____________________________________________________


# ============================================================
# SECTION 4 — ESTIMATE A PROBABILITY WITH REPEATED TRIALS
# ============================================================
def estimate_heads(trials, seed=42):
    if trials <= 0:
        raise ValueError("trials must be positive")
    rng = random.Random(seed)
    heads = 0
    for _ in range(trials):
        if rng.random() < 0.5:
            heads += 1
    return heads / trials


# The function expects an integer trial count.
# print(estimate_heads(10))
# print(estimate_heads(10000))
# Larger samples typically give more stable estimates, but do not
# guarantee a closer answer on every run. The target here is 0.5.
# EXERCISE 4 — EXPLAIN
# Why reject trials=0 before dividing?
# ANSWER: ____________________________________________________


# ============================================================
# SECTION 5 — TWO DICE DO NOT HAVE UNIFORM SUMS
# ============================================================
def example_dice_distribution():
    rng = random.Random(42)
    totals = Counter()
    trials = 10000
    for _ in range(trials):
        total = rng.randint(1, 6) + rng.randint(1, 6)
        totals[total] += 1
    for total in range(2, 13):
        print(total, totals[total], f"{totals[total] / trials:.1%}")


# example_dice_distribution()
# One ordered pair sums to 2: (1, 1).
# Six pairs sum to 7: (1, 6), (2, 5), (3, 4), (4, 3), (5, 2), (6, 1).
# randint(2, 12) instead makes all eleven sums equally likely.
# The generation method determines the distribution being modeled.
# EXERCISE 5 — COUNT
# How many ordered pairs sum to 12? ________ To 3? ________


# ============================================================
# SECTION 6 — LIMITS OF SIMULATIONS
# ============================================================
# A simulation estimates behavior under the assumptions you encode.
# More trials reduce sampling noise but do not repair a wrong model.
# Independent trials do not remember streaks: several heads in a row
# do not make tails more likely on the next fair-coin trial.
# Fixed seeds help reproduce results. Selecting only favorable seeds
# gives a misleading picture of typical outcomes.


# ============================================================
# SECTION 7 — CODING CHALLENGES
# ============================================================
# CHALLENGE 1: Generate 100 uniform values between 5 and 15.
# Print min, max, and arithmetic mean using sum()/len().
# Explain why the sample mean need not equal exactly 10.
# Write your code here:


# CHALLENGE 2: Estimate the probability that two dice sum to 7.
# Accept a positive integer trial count and a seed. Compare the
# estimate to 6/36 without demanding exact equality.
# Write your code here:


# CHALLENGE 3: Simulate a 30% success chance over 1000 trials.
# Return successes, failures, and observed success proportion.
# Verify successes + failures equals the requested trial count.
# Write your code here:


# ============================================================
# SECTION 8 — FINAL REVIEW
# ============================================================
# 1. Which function selects floats between bounds? ______________
# 2. How does Gaussian differ from uniform? ____________________
# 3. Are Gaussian values confined to mu +/- sigma? _____________
# 4. Why draw integer cents for equally likely cent amounts? ____
# 5. Why isn't randint(2, 12) equivalent to rolling two dice? ____
# 6. Does a streak affect the next independent trial's chance? __
# 7. Can more trials fix an incorrect model? ___________________
#
# KEY TAKEAWAY:
# Match the distribution to the process being modeled. Summarize
# many trials, distinguish estimates from guarantees, and keep
# experiments reproducible when comparing results.
# ============================================================
# END OF LESSON
# ============================================================
