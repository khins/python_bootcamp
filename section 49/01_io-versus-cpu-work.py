# ============================================================
# FILE: 01_io-versus-cpu-work.py
# TOPIC: Choose When Threads Help
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call at a time.
# Expected results appear beside examples. Timing/order may vary where noted.
# Complete the practice yourself; example solutions are separate from practice.
# See learning-guide.txt for section order, setup, and project instructions.

# LESSON OBJECTIVES
# 1. Distinguish waiting from computation.
# 2. Understand interpreter-dependent CPU parallelism.

# SECTION 1 - UNDERSTAND THE IDEA
# Threads can overlap waits for network or disk I/O. In standard GIL-enabled
# CPython, Python-bytecode CPU work generally does not run in parallel across
# threads. Some native libraries release the GIL; optional free-threaded builds
# have different behavior. Never use the GIL as an application lock. This
# section uses finite simulated I/O, not real internet downloads by default.

# SECTION 2 - WORKED EXAMPLES
from time import sleep

def simulated_read(title):
    sleep(0.005)  # A tiny finite stand-in for I/O waiting.
    return title.upper()

def example_io():
    print(simulated_read("Signals"))  # => SIGNALS

# example_io()

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Classify downloading bytes, parsing JSON, and sorting a large list.
# ANSWER / CODE: ______________________________________________
# 2. Explain why more workers can overload a server instead of helping.
# ANSWER / CODE: ______________________________________________
# 3. Compare threads with processes conceptually for CPU-heavy Python work.
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: Choose concurrency based on the work and runtime, then measure.

# ============================================================
# END OF LESSON
# ============================================================
