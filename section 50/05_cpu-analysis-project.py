# ============================================================
# FILE: 05_cpu-analysis-project.py
# TOPIC: Project: Compare Sequential and Process Analysis
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call.
# Run the file as a script, especially for process examples on Windows.
# See learning-guide.txt for dependencies, setup, and the section project.
#
# LESSON OBJECTIVES
# - Explain the behavior demonstrated below and predict its result.
# - Apply project: compare sequential and process analysis to a small independent exercise.
# - Identify the limitations and failure cases described in the notes.

# ============================================================
# SECTION 1 — UNDERSTAND THE IDEA
# ============================================================
# The companion cpu_analysis.py computes the same sum-of-squares tasks in two
# ways and measures complete execution, including process startup. Equal results
# are required; a speedup is not. Use representative workloads and repeated
# measurements. Do not compare different algorithms and label the difference
# purely a multiprocessing speedup. Empty input should produce no results.

# ============================================================
# SECTION 2 — WORKED EXAMPLE
# ============================================================
from cpu_analysis import compare

def example():
    results, sequential, parallel = compare([3, 4, 5])
    print(results)  # => [5, 14, 30]
    print(sequential, parallel)  # Timings vary; small tasks often favor sequential.


# Keep the call under this guard; imports should not launch examples.
if __name__ == "__main__":
    # example()
    pass

# ============================================================
# SECTION 3 — PREDICT, PRACTICE, AND FINAL REVIEW
# ============================================================
# 1. Which costs are included in the process timing?
# ANSWER / CODE: ______________________________________________

# 2. CHALLENGE: Add repeated measurements and report the median, preserving result checks.
# ANSWER / CODE: ______________________________________________

# 3. Test empty input, negative limits, and invalid worker counts.
# ANSWER / CODE: ______________________________________________

# KEY TAKEAWAY: The companion cpu_analysis.py computes the same sum-of-squares
# tasks in two ways and measures complete execution, including process
# startup.
# ============================================================
# END OF LESSON
# ============================================================
