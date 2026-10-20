# ============================================================
# FILE: 04_seeds-and-reproducible-randomness.py
# TOPIC: Deep Dive — Seeds and Independent Generators
# ============================================================
# LESSON OBJECTIVES
# 1. Explain how seeds control pseudorandom sequences.
# 2. Repeat an experiment using a fixed seed.
# 3. Isolate randomness with random.Random instances.
# 4. Check reliable properties of random behavior.
#
# Uncomment individual example calls. Local generators keep these
# examples from changing the module-level generator's state.

import random


# ============================================================
# SECTION 1 — A GENERATOR HAS STATE
# ============================================================
# Each draw advances internal state. A seed initializes that state.
# Repeating a seed and the same calls reproduces the sequence in
# the same environment; it does not make every draw the same.

def example_same_seed():
    first = random.Random(42)
    second = random.Random(42)
    first_rolls = [first.randint(1, 6) for _ in range(8)]
    second_rolls = [second.randint(1, 6) for _ in range(8)]
    print(first_rolls)
    print(second_rolls)
    print(first_rolls == second_rolls) # => True


# example_same_seed()
# EXERCISE 1 — EXPLAIN
# Why are the lists equal even though their values are random?
# ANSWER: ____________________________________________________


# ============================================================
# SECTION 2 — GLOBAL SEEDING VERSUS LOCAL GENERATORS
# ============================================================
# random.seed(42) resets the module-level generator used by calls
# such as random.randint(), random.choice(), and random.shuffle().
# Other code drawing from that generator can affect your sequence.
# random.Random(42) creates an independent generator instead.

def example_local_generator():
    rng = random.Random(12)
    print(rng.choice(["heads", "tails"]))
    print(rng.sample(range(10), k=3))
    values = [1, 2, 3, 4]
    rng.shuffle(values)
    print(values)


# example_local_generator()
# A Random instance provides the same core methods as the module.
# rng is a conventional name meaning random number generator.
# EXERCISE 2 — EXPLAIN
# Why might independent simulations use separate generators?
# ANSWER: ____________________________________________________


# ============================================================
# SECTION 3 — SEED ONCE, THEN DRAW MANY TIMES
# ============================================================
def example_reseeding_mistake():
    repeated = [random.Random(7).random() for _ in range(3)]
    rng = random.Random(7)
    sequence = [rng.random() for _ in range(3)]
    print(repeated) # The same first draw repeated three times.
    print(sequence) # Three successive draws from one generator.


# example_reseeding_mistake()
# Creating a new generator with the same seed inside a loop restarts
# the sequence every iteration. Usually initialize before the loop.
# EXERCISE 3 — FIX
# Where should rng = random.Random(7) go for ten successive dice rolls?
# ANSWER: ____________________________________________________


# ============================================================
# SECTION 4 — SAVE AND RESTORE STATE
# ============================================================
def example_restore_state():
    rng = random.Random(21)
    saved = rng.getstate()
    first = [rng.random() for _ in range(3)]
    rng.setstate(saved)
    replay = [rng.random() for _ in range(3)]
    print(first == replay) # => True


# example_restore_state()
# Treat state as opaque: pass it to setstate(), rather than editing it.
# This lets you replay part of an experiment from the same point.


# ============================================================
# SECTION 5 — REPRODUCIBILITY HAS SEVERAL INPUTS
# ============================================================
# Preserve the seed, input ordering, parameters, and order of calls.
# An extra draw consumes state and can change later results.
# Different seeds can still give the same individual draw.
# Higher-level algorithms can change across Python versions; record
# your version when an experiment requires exact replay.
# Seeding makes results predictable, not secure.


# ============================================================
# SECTION 6 — CHECK PROPERTIES, NOT A LUCKY OUTPUT
# ============================================================
def example_check_properties():
    rng = random.Random(100)
    rolls = [rng.randint(1, 6) for _ in range(100)]
    print(len(rolls) == 100)                     # => True
    print(all(1 <= roll <= 6 for roll in rolls)) # => True
    picks = rng.sample(range(20), k=5)
    print(len(picks) == len(set(picks)) == 5)    # => True


# example_check_properties()
# Do not demand that every face appear in a small set of dice rolls.
# Bounds, size, and uniqueness (when promised) are dependable checks.
# EXERCISE 4 — EXPLAIN
# Why might checking for exactly five sixes in 30 rolls fail?
# ANSWER: ____________________________________________________


# ============================================================
# SECTION 7 — CODING CHALLENGES
# ============================================================
# CHALLENGE 1: Write simulate_rolls(count, seed). Create one local
# generator and return count six-sided dice rolls. Compare two
# calls with the same arguments.
# Write your code here:


# CHALLENGE 2: Write pick_team(players, size, rng). Use rng.sample().
# Try two separate Random instances with the same seed. Explain
# how accepting rng gives the caller control of randomness.
# Write your code here:


# ============================================================
# SECTION 8 — FINAL REVIEW
# ============================================================
# 1. What does a seed initialize? ______________________________
# 2. Should you normally reseed before every draw? _____________
# 3. How do you create an independent generator? _______________
# 4. Which methods save and restore state? _____________________
# 5. Why can an extra draw change later results? _______________
# 6. Does seeding make random suitable for passwords? __________
#
# KEY TAKEAWAY:
# Seed once for repeatable experiments. Use local Random instances
# to isolate state and check the properties your program promises.
# ============================================================
# END OF LESSON
# ============================================================
