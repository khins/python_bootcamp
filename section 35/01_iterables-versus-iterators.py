# ============================================================
# FILE: 01_iterables-versus-iterators.py
# TOPIC: Iterables versus Iterators
# ============================================================
# STUDY GUIDE
# Predict before running. Uncomment individual example calls.
# Expected outputs appear in comments. Complete the exercises yourself.
# All examples use the standard library; no packages need installation.

# LESSON OBJECTIVES
# 1. Distinguish an iterable from an iterator.
# 2. Create independent traversal positions.

# SECTION 1 — A COLLECTION AND ITS TRAVERSAL
# An iterable can supply an iterator through iter().
# An iterator supplies successive values through next() and remembers
# its current position. Iterators are themselves iterable.
# A list can supply fresh iterators. A list iterator is a traversal,
# not a second copy of the list.

def example_list_and_iterator():
    albums = ["Signals", "Blue", "Kind of Blue"]
    cursor = iter(albums)
    print(next(cursor))         # => Signals
    print(next(cursor))         # => Blue
    print(albums)               # => ['Signals', 'Blue', 'Kind of Blue']
    print(iter(cursor) is cursor)  # => True


# example_list_and_iterator()
# next(albums) would raise TypeError: the list is not itself an iterator.
# iter(albums) creates a new list iterator; it does not consume an item.


# SECTION 2 — TWO INDEPENDENT POSITIONS
def example_independent_iterators():
    albums = ["Signals", "Blue"]
    first = iter(albums)
    second = iter(albums)
    print(next(first))   # => Signals
    print(next(first))   # => Blue
    print(next(second))  # => Signals
    print(first is second)  # => False


# example_independent_iterators()
# Strings, tuples, dictionaries, sets, and ranges are also iterable.
# Dictionary iteration yields keys. Set iteration has no useful
# positional order to depend on.

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Explain why next(iter(albums)) twice returns the first album twice.
# ANSWER / CODE: ______________________________________________
# 2. Create an iterator over a string and consume two characters.
# ANSWER / CODE: ______________________________________________
# 3. Does creating an iterator copy all of the source data?
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: An iterable supplies traversal; an iterator tracks traversal state.

# ============================================================
# END OF LESSON
# ============================================================

