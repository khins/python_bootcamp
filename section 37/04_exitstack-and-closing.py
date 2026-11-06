# ============================================================
# FILE: 04_exitstack-and-closing.py
# TOPIC: Compose Cleanup with ExitStack
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call at a time.
# Expected results appear beside examples. Timing/order may vary where noted.
# Complete the practice yourself; example solutions are separate from practice.
# See learning-guide.txt for section order, setup, and project instructions.

# LESSON OBJECTIVES
# 1. Manage a dynamic number of resources.
# 2. Adapt an object exposing close().

# SECTION 1 - UNDERSTAND THE IDEA
# ExitStack collects cleanup actions and unwinds them in reverse registration
# order. enter_context enters a manager and registers its exit. If later entry
# fails, earlier resources are still released. closing adapts a close method;
# it does not catch or hide body errors.

# SECTION 2 - WORKED EXAMPLES
from contextlib import ExitStack, closing
from io import StringIO

def example_stack():
    events = []
    with ExitStack() as stack:
        stack.callback(events.append, "first")
        stack.callback(events.append, "second")
        streams = [stack.enter_context(StringIO(text)) for text in ["Rush", "Yes"]]
        print([s.read() for s in streams])  # => ['Rush', 'Yes']
    print(events)                           # => ['second', 'first']
    print(all(s.closed for s in streams))   # => True
    with closing(StringIO("Blue")) as stream:
        print(stream.read())                # => Blue

# example_stack()

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Register three callbacks and predict their order.
# ANSWER / CODE: ______________________________________________
# 2. Use ExitStack to open two temporary files.
# ANSWER / CODE: ______________________________________________
# 3. Explain why a resource must be registered immediately after acquisition.
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: Register cleanup as resources are acquired, then unwind in reverse.

# ============================================================
# END OF LESSON
# ============================================================
