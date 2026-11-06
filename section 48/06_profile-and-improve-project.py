# ============================================================
# FILE: 06_profile-and-improve-project.py
# TOPIC: Project: Improve a Listening Analyzer
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call at a time.
# Expected results appear beside examples. Timing/order may vary where noted.
# Complete the practice yourself; example solutions are separate from practice.
# See learning-guide.txt for section order, setup, and project instructions.

# LESSON OBJECTIVES
# 1. Measure a concrete repeated-work bottleneck.
# 2. Verify equal results and compare time/memory.

# SECTION 1 - UNDERSTAND THE IDEA
# The baseline counts each distinct artist with a fresh full list scan. With u
# distinct artists and n events that is O(n*u), worst-case O(n^2). Counter scans
# once with expected O(n) work and O(u) summary storage. The benchmark includes
# high-cardinality synthetic input so repeated scanning is visible. No fixed
# speedup is promised. Both algorithms still retain their result dictionaries.

# SECTION 2 - WORKED EXAMPLES
from collections import Counter
from timeit import repeat
import cProfile
import pstats
import tracemalloc

def baseline(events):
    return {artist: events.count(artist) for artist in dict.fromkeys(events)}

def improved(events):
    return dict(Counter(events))

def peak_for(function, events):
    tracemalloc.start()
    try:
        result = function(events)
        return tracemalloc.get_traced_memory()[1], len(result)
    finally:
        tracemalloc.stop()

def example_optimization_project():
    events = [f"Artist {n % 400}" for n in range(4000)]
    for sample in [[], ["Rush"], ["Rush", "Yes", "Rush"], events]:
        assert baseline(sample) == improved(sample)
    profiler = cProfile.Profile()
    profiler.runcall(baseline, events)
    pstats.Stats(profiler).strip_dirs().sort_stats("cumulative").print_stats(5)
    for function in [baseline, improved]:
        seconds = min(repeat(lambda: function(events), number=3, repeat=3)) / 3
        peak, distinct = peak_for(function, events)
        print(function.__name__, seconds, peak, distinct)  # Timings/bytes vary; distinct=400.

# example_optimization_project()

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Record measurements for 1, 10, and 400 distinct artists.
# ANSWER / CODE: ______________________________________________
# 2. Explain why the improvement depends on cardinality as well as event count.
# ANSWER / CODE: ______________________________________________
# 3. Optimize your own analyzer and preserve its invalid-input behavior.
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: A measured change should retain behavior and explain the source of improvement.

# ============================================================
# END OF LESSON
# ============================================================
