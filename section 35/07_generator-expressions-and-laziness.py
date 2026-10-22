# ============================================================
# FILE: 07_generator-expressions-and-laziness.py
# TOPIC: Generator Expressions and Lazy Evaluation
# ============================================================
# STUDY GUIDE
# Predict before running. Uncomment individual example calls.
# Expected outputs appear in comments. Complete the exercises yourself.
# All examples use the standard library; no packages need installation.

# LESSON OBJECTIVES
# 1. Compare list comprehensions with generator expressions.
# 2. Explain when computation happens.

# SECTION 1 — MATERIALIZE NOW OR COMPUTE ON DEMAND
def example_expression():
    squares_list = [number * number for number in range(4)]
    squares_stream = (number * number for number in range(4))
    print(squares_list)          # => [0, 1, 4, 9]
    print(next(squares_stream))  # => 0
    print(list(squares_stream))  # => [1, 4, 9]


# example_expression()
# [] builds a list immediately. () creates a generator expression.
# A generator avoids holding all result values at once, but may retain
# references to its input. Laziness does not make the input disappear.


# SECTION 2 — TRANSFORMATIONS HAPPEN ON DEMAND
def example_observe_evaluation():
    def square(number):
        print("Calculating", number)
        return number * number

    results = (square(number) for number in range(3))
    print("Ready")        # => Ready
    print(next(results))  # => Calculating 0, then 0
    print(sum(results))   # => Calculating 1, Calculating 2, then 5


# example_observe_evaluation()


# SECTION 3 — LATE USE OF VARIABLES
def example_variable_timing():
    factor = 2
    results = (number * factor for number in [1, 2])
    factor = 10
    print(list(results))  # => [10, 20]


# example_variable_timing()
# The leftmost iterable expression is evaluated and its iterator obtained
# when the generator expression is created. Its item transformations and
# filters run later. Avoid describing every part as deferred.

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Convert a list comprehension filtering long album names to a generator.
# ANSWER / CODE: ______________________________________________
# 2. Why can changing factor before consumption change the result?
# ANSWER / CODE: ______________________________________________
# 3. Compare sum(n * n for n in range(4)) with storing a list first.
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: Lazy transformations run when the consumer requests their values.

# ============================================================
# END OF LESSON
# ============================================================

