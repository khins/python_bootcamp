# ============================================================
# FILE: 02_enter-and-exit.py
# TOPIC: Write a Context Manager Class
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call at a time.
# Expected results appear beside examples. Timing/order may vary where noted.
# Complete the practice yourself; example solutions are separate from practice.
# See learning-guide.txt for section order, setup, and project instructions.

# LESSON OBJECTIVES
# 1. Return the as-binding from __enter__.
# 2. Propagate exceptions from __exit__.

# SECTION 1 - UNDERSTAND THE IDEA
# __enter__ returns the value assigned after as; it need not return self.
# __exit__ receives exception type, value, and traceback, or three None values
# on normal completion. Returning False/None propagates an exception; True
# suppresses it. Suppress only errors your manager intentionally handles.

# SECTION 2 - WORKED EXAMPLES
class TraceScope:
    def __enter__(self):
        print("enter")
        return "resource"

    def __exit__(self, exc_type, exc_value, traceback):
        print("exit:", exc_type.__name__ if exc_type else "normal")
        return False

def example_protocol():
    with TraceScope() as value:
        print(value)
    # => enter / resource / exit: normal (three lines)
    try:
        with TraceScope():
            raise ValueError("problem")
    except ValueError:
        print("caught outside")
    # => enter / exit: ValueError / caught outside

# example_protocol()

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Change the as value to a dictionary.
# ANSWER / CODE: ______________________________________________
# 2. Explain the consequences of returning True unconditionally.
# ANSWER / CODE: ______________________________________________
# 3. Write a manager that records entry and exit events in a list.
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: The exit return value controls propagation, not the body result.

# ============================================================
# END OF LESSON
# ============================================================
