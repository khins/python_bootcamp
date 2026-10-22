# ============================================================
# FILE: 09_yield-from-and-generator-return.py
# TOPIC: Delegation with yield from
# ============================================================
# STUDY GUIDE
# Predict before running. Uncomment individual example calls.
# Expected outputs appear in comments. Complete the exercises yourself.
# All examples use the standard library; no packages need installation.

# LESSON OBJECTIVES
# 1. Delegate to another iterable.
# 2. Distinguish yielded values from a generator's return value.

# SECTION 1 — YIELD ONE OBJECT OR ITS ELEMENTS
def yield_collection():
    yield ["Signals", "Blue"]


def yield_elements():
    yield from ["Signals", "Blue"]


def example_delegation():
    print(list(yield_collection()))  # => [['Signals', 'Blue']]
    print(list(yield_elements()))    # => ['Signals', 'Blue']


# example_delegation()


# SECTION 2 — FLATTEN ONE LEVEL
def flatten(groups):
    for group in groups:
        yield from group


def example_flatten():
    print(list(flatten([[1, 2], [], [3]])))  # => [1, 2, 3]
    print(list(flatten(["ab", "cd"])))       # => ['a', 'b', 'c', 'd']


# example_flatten()
# This flattens exactly one level; it is not a recursive flattener.
# Strings are iterable, so they are delegated character by character.


# SECTION 3 — return ENDS THE GENERATOR
def measured_items():
    yield "Signals"
    yield "Blue"
    return 2


def catalog_with_summary():
    count = yield from measured_items()
    yield f"Processed {count} albums"


def example_return_value():
    print(list(measured_items()))  # => ['Signals', 'Blue']
    print(list(catalog_with_summary()))
    # => ['Signals', 'Blue', 'Processed 2 albums']


# example_return_value()
# A generator's return value becomes StopIteration.value, not another item.
# yield from can capture that completion value.
# Use return to stop a generator. Explicitly raising StopIteration inside
# its body causes RuntimeError when it escapes; this differs from __next__.

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Write a generator that delegates to two playlists in sequence.
# ANSWER / CODE: ______________________________________________
# 2. Why is 2 absent from list(measured_items())?
# ANSWER / CODE: ______________________________________________
# 3. Contrast raising StopIteration in __next__ with return in a generator.
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: yield from delegates iteration and can receive a completion value.

# ============================================================
# END OF LESSON
# ============================================================

