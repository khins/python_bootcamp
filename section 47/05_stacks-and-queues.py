# ============================================================
# FILE: 05_stacks-and-queues.py
# TOPIC: Model LIFO and FIFO Work
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call at a time.
# Expected results appear beside examples. Timing/order may vary where noted.
# Complete the practice yourself; example solutions are separate from practice.
# See learning-guide.txt for section order, setup, and project instructions.

# LESSON OBJECTIVES
# 1. Use list for a stack and deque for a queue.
# 2. Predict processing order.

# SECTION 1 - UNDERSTAND THE IDEA
# Stacks are last-in-first-out: append/pop on a list. Queues are first-in-first-out:
# append/popleft on a deque. list.pop(0) shifts remaining items and costs O(n).
# These processing orders support depth-first and breadth-first traversals.
# Choose the data structure for the operations you actually perform.

# SECTION 2 - WORKED EXAMPLES
from collections import deque

def example_orders():
    stack = ["A", "B", "C"]
    queue = deque(stack)
    print([stack.pop() for _ in range(3)])    # => ['C', 'B', 'A']
    print([queue.popleft() for _ in range(3)])  # => ['A', 'B', 'C']

# example_orders()

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Model undo with a stack.
# ANSWER / CODE: ______________________________________________
# 2. Model pending downloads with a queue.
# ANSWER / CODE: ______________________________________________
# 3. Explain the time cost of draining a list with pop(0).
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: LIFO and FIFO are behavior contracts supported by different operations.

# ============================================================
# END OF LESSON
# ============================================================
