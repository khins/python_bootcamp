# ============================================================
# FILE: 06_timeouts-and-cancellation.py
# TOPIC: Understand Future Timeouts
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call at a time.
# Expected results appear beside examples. Timing/order may vary where noted.
# Complete the practice yourself; example solutions are separate from practice.
# See learning-guide.txt for section order, setup, and project instructions.

# LESSON OBJECTIVES
# 1. Distinguish waiting timeout from stopping work.
# 2. Cancel only pending work.

# SECTION 1 - UNDERSTAND THE IDEA
# future.result(timeout=...) limits the caller's wait; it does not kill a running
# thread. cancel succeeds only before a task starts. Exiting an executor context
# normally waits for running work, even after a result timeout. Bound I/O inside
# the worker itself. Threads need cooperative cancellation, often with Event.

# SECTION 2 - WORKED EXAMPLES
from concurrent.futures import Future
from threading import Event

def example_cancellation():
    pending = Future()
    print(pending.cancel())     # => True
    print(pending.cancelled())  # => True
    running = Future()
    running.set_running_or_notify_cancel()
    print(running.cancel())     # => False
    running.set_result("done")
    print(running.result())     # => done
    stop = Event()
    stop.set()
    print(stop.is_set())        # => True

# example_cancellation()

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Describe where a worker should check a stop Event.
# ANSWER / CODE: ______________________________________________
# 2. Explain why a future timeout is not an HTTP read timeout.
# ANSWER / CODE: ______________________________________________
# 3. Design shutdown behavior for pending versus running downloads.
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: Waiting less is not the same as stopping the underlying task.

# ============================================================
# END OF LESSON
# ============================================================
