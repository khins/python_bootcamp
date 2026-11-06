# ============================================================
# FILE: 04_itertools-pipelines.py
# TOPIC: Compose Iterators
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call at a time.
# Expected results appear beside examples. Timing/order may vary where noted.
# Complete the practice yourself; example solutions are separate from practice.
# See learning-guide.txt for section order, setup, and project instructions.

# LESSON OBJECTIVES
# 1. Chain and slice lazy inputs.
# 2. Bound infinite iterators.

# SECTION 1 - UNDERSTAND THE IDEA
# itertools supplies iterator building blocks. chain joins inputs lazily;
# islice selects positions without building a full list. count never finishes,
# so always bound consumption. product emits combinations but first pools its
# inputs; do not give it an infinite iterable. Iterators are consumed once.

# SECTION 2 - WORKED EXAMPLES
from itertools import chain, count, islice, product

def example_pipeline():
    titles = chain(["YYZ", "Blue"], ["Roundabout"])
    print(list(islice(titles, 2)))  # => ['YYZ', 'Blue']
    print(list(titles))            # => ['Roundabout']
    print(list(islice(count(100, 10), 3)))  # => [100, 110, 120]
    print(list(product(["Rush", "Yes"], ["CD", "LP"])))
    # => [('Rush', 'CD'), ('Rush', 'LP'), ('Yes', 'CD'), ('Yes', 'LP')]

# example_pipeline()

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Chain three playlists and take the first five titles.
# ANSWER / CODE: ______________________________________________
# 2. Explain why list(count()) never completes.
# ANSWER / CODE: ______________________________________________
# 3. Generate all artist/format pairs for two small lists.
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: Laziness saves intermediate storage only when consumption stays bounded.

# ============================================================
# END OF LESSON
# ============================================================
