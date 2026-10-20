# ============================================================
# FILE: 03_the-shuffle-function.py
# TOPIC: Reordering Lists with shuffle
# ============================================================
# LESSON OBJECTIVES
# 1. Shuffle a list in place.
# 2. Understand mutation, None returns, and shared references.
# 3. Preserve an original sequence when needed.
# 4. Deal entries from a shuffled list.
#
# Predict before running. Uncomment individual example calls.

import random


# ============================================================
# SECTION 1 — shuffle(): CHANGE ORDER IN PLACE
# ============================================================
def example_shuffle():
    playlist = ["Song A", "Song B", "Song C", "Song D"]
    random.shuffle(playlist)
    print(playlist) # Same songs, potentially a different order.


# example_shuffle()
# shuffle() changes the existing list without adding or removing items.
# The original order is also a possible random result.
# Two shuffles are not guaranteed to produce different orders.
# EXERCISE 1 — EXPLAIN
# Does an unchanged order necessarily indicate a bug?
# ANSWER: ____________________________________________________


# ============================================================
# SECTION 2 — THE RETURN VALUE IS None
# ============================================================
def example_return_value():
    numbers = [1, 2, 3, 4]
    result = random.shuffle(numbers)
    print(result)  # => None
    print(numbers) # The shuffled list still lives here.


# example_return_value()
# Avoid: numbers = random.shuffle(numbers)
# That assignment replaces your list reference with None.
# Like list.sort(), shuffle() works by mutating the list.
# EXERCISE 2 — FIX
# Fix: playlist = random.shuffle(playlist)
# ANSWER: ____________________________________________________


# ============================================================
# SECTION 3 — COPY FIRST TO PRESERVE THE ORIGINAL
# ============================================================
def example_shuffle_copy():
    original = ["intro", "verse", "chorus", "outro"]
    randomized = original.copy()
    random.shuffle(randomized)
    print(original)   # => ['intro', 'verse', 'chorus', 'outro']
    print(randomized) # Same entries in random order.
    print(original is randomized) # => False


# example_shuffle_copy()
# copy() creates a shallow copy: a separate outer list.
# Nested objects remain shared, but rearranging the outer copy
# does not rearrange the original outer list.


# ============================================================
# SECTION 4 — ASSIGNMENT DOES NOT COPY A LIST
# ============================================================
def example_alias():
    original = [1, 2, 3, 4]
    alias = original
    random.shuffle(alias)
    print(alias is original) # => True
    print(alias == original) # => True


# example_alias()
# Both names refer to the same list and observe the same new order.
# EXERCISE 3 — EXPLAIN
# How does alias = original differ from alias = original.copy()?
# ANSWER: ____________________________________________________


# ============================================================
# SECTION 5 — IMMUTABLE SEQUENCES NEED A NEW LIST
# ============================================================
def example_tuple_order():
    source = ("north", "south", "east", "west")
    reordered = random.sample(source, k=len(source))
    print(reordered) # A new list containing all four entries.
    print(source)    # The original tuple is unchanged.


# example_tuple_order()
# shuffle() requires a mutable sequence, such as a list.
# Tuples and strings cannot be shuffled directly.
# Alternative: items = list(source), then random.shuffle(items).
# Empty and one-item lists can be shuffled; their order cannot change.


# ============================================================
# SECTION 6 — SHUFFLE ONCE, THEN DEAL
# ============================================================
def example_deal():
    deck = list(range(1, 11))
    random.shuffle(deck)
    first_hand = deck[:3]
    second_hand = deck[3:6]
    remaining = deck[6:]
    print(first_hand)
    print(second_hand)
    print(remaining)


# example_deal()
# Non-overlapping slices partition the shuffled entries.
# Slicing does not remove entries from deck; these are new lists.
# Two independent sample(deck, k=3) calls could overlap because
# each call starts with the full deck. A shuffle plus disjoint
# slices avoids overlap for this deck of unique values.
# EXERCISE 4 — COUNT
# How many entries remain after both hands? ____________________


# ============================================================
# SECTION 7 — CODING CHALLENGES
# ============================================================
# CHALLENGE 1: Write shuffled_copy(items). Return a shuffled list
# without changing the supplied sequence. Test a list and a tuple.
# Write your code here:


# CHALLENGE 2: Shuffle eight unique players into two teams of four.
# Preserve a separate copy of the original signup order.
# Write your code here:


# ============================================================
# SECTION 8 — FINAL REVIEW
# ============================================================
# 1. What does shuffle() return? _______________________________
# 2. What does in place mean? _________________________________
# 3. Does assigning a list to another name copy it? _____________
# 4. Can you shuffle a tuple directly? ________________________
# 5. How can sample() create a full reordered copy? ____________
# 6. Can a valid shuffle preserve the original order? __________
#
# KEY TAKEAWAY:
# shuffle() mutates a list and returns None. Copy first when the
# original order matters, or use sample() for a reordered copy.
# ============================================================
# END OF LESSON
# ============================================================
