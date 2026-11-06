# ============================================================
# FILE: 03_deque.py
# TOPIC: Queues and Recent History
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call at a time.
# Expected results appear beside examples. Timing/order may vary where noted.
# Complete the practice yourself; example solutions are separate from practice.
# See learning-guide.txt for section order, setup, and project instructions.

# LESSON OBJECTIVES
# 1. Use both ends of a deque.
# 2. Explain maxlen eviction.

# SECTION 1 - UNDERSTAND THE IDEA
# A deque supports efficient append/pop operations at both ends. popleft()
# implements a FIFO queue without shifting a whole list. A bounded deque drops
# items from the opposite end when an append exceeds maxlen; it is not storage
# for records you must never lose. Indexing the middle is not its strength.

# SECTION 2 - WORKED EXAMPLES
from collections import deque

def example_queue():
    pending = deque(["YYZ", "Roundabout"])
    print(pending.popleft())  # => YYZ
    pending.append("Blue")
    print(list(pending))      # => ['Roundabout', 'Blue']
    recent = deque(maxlen=2)
    recent.extend(["A", "B", "C"])
    print(list(recent))       # => ['B', 'C']
    recent.appendleft("D")
    print(list(recent))       # => ['D', 'B']

# example_queue()

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Build a queue that processes three song requests in arrival order.
# ANSWER / CODE: ______________________________________________
# 2. Predict appendleft on a full deque.
# ANSWER / CODE: ______________________________________________
# 3. Handle popping an empty queue explicitly.
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: Choose deque for end operations and deliberate bounded history.

# ============================================================
# END OF LESSON
# ============================================================
