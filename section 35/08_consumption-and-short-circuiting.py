# ============================================================
# FILE: 08_consumption-and-short-circuiting.py
# TOPIC: Consumption and Short-Circuiting
# ============================================================
# STUDY GUIDE
# Predict before running. Uncomment individual example calls.
# Expected outputs appear in comments. Complete the exercises yourself.
# All examples use the standard library; no packages need installation.

# LESSON OBJECTIVES
# 1. Identify consumers that exhaust an iterator.
# 2. Observe partial consumption by any and all.

# SECTION 1 — AGGREGATION USES UP INPUT
def example_exhausting_consumers():
    numbers = (number for number in [1, 2, 3])
    print(sum(numbers))   # => 6
    print(list(numbers)) # => []
    print(sum(numbers))  # => 0


# example_exhausting_consumers()
# list(), tuple(), sorted(), and sum() consume finite iterators to the end.
# list and sorted materialize results, losing streaming memory benefits.
# len(generator) and generator[0] are not supported.


# SECTION 2 — SOME CONSUMERS STOP EARLY
def example_short_circuit():
    values = iter([0, 0, 7, 9])
    print(any(values))   # => True
    print(next(values))  # => 9

    values = iter([1, 2, 0, 4])
    print(all(values))   # => False
    print(next(values))  # => 4


# example_short_circuit()
# any stops on the first truthy item; all stops on the first falsey item.
# The deciding item is consumed too. Remaining items stay available.
# On empty input, any returns False and all returns True.


# SECTION 3 — RECREATE OR MATERIALIZE INTENTIONALLY
def example_two_passes():
    def numbers():
        yield from [1, 2, 3]

    print(sum(numbers()))  # => 6
    print(max(numbers()))  # => 3


# example_two_passes()
# Each numbers() call creates a new traversal. This is appropriate when
# the data can be obtained again. For a small one-time source, materializing
# once may be the clearer choice.
# yield from is explained fully in the next lesson.

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Predict the remaining items after '2 in iter([1, 2, 3])' using a named iterator.
# ANSWER / CODE: ______________________________________________
# 2. Why does computing sum and then max on one generator fail?
# ANSWER / CODE: ______________________________________________
# 3. Create a fresh generator for each of two independent calculations.
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: Consumers advance iterators; plan explicitly for multiple passes.

# ============================================================
# END OF LESSON
# ============================================================

