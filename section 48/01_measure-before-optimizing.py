# ============================================================
# FILE: 01_measure-before-optimizing.py
# TOPIC: Start with a Correct Baseline
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call at a time.
# Expected results appear beside examples. Timing/order may vary where noted.
# Complete the practice yourself; example solutions are separate from practice.
# See learning-guide.txt for section order, setup, and project instructions.

# LESSON OBJECTIVES
# 1. Define the workload and metric.
# 2. Preserve behavior while optimizing.

# SECTION 1 - UNDERSTAND THE IDEA
# Optimization begins with a representative workload and a correct result.
# Specify whether you care about latency, throughput, or memory. Measure a
# baseline, locate the expensive part, change one thing, and remeasure. Small
# synthetic examples teach tools but may not predict production behavior.

# SECTION 2 - WORKED EXAMPLES
def count_plays(artists):
    counts = {}
    for artist in artists:
        counts[artist] = counts.get(artist, 0) + 1
    return counts

def example_baseline():
    assert count_plays(["Rush", "Yes", "Rush"]) == {"Rush": 2, "Yes": 1}
    assert count_plays([]) == {}
    print("baseline verified")  # => baseline verified

# example_baseline()

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Write down input size, expected output, and metric before timing.
# ANSWER / CODE: ______________________________________________
# 2. Identify an unrepresentative benchmark input.
# ANSWER / CODE: ______________________________________________
# 3. Explain why faster wrong output is not an improvement.
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: Measure a defined workload only after checking correctness.

# ============================================================
# END OF LESSON
# ============================================================
