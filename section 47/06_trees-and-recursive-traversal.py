# ============================================================
# FILE: 06_trees-and-recursive-traversal.py
# TOPIC: Traverse a Tree
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call at a time.
# Expected results appear beside examples. Timing/order may vary where noted.
# Complete the practice yourself; example solutions are separate from practice.
# See learning-guide.txt for section order, setup, and project instructions.

# LESSON OBJECTIVES
# 1. Define a base case.
# 2. Recognize depth and cycle limits.

# SECTION 1 - UNDERSTAND THE IDEA
# A tree has a root and children; each non-root node has one parent. Recursive
# traversal visits a node then its children, stopping at leaves. A general graph
# can have cycles and needs a visited set. Deep trees can exceed Python's
# recursion limit; an explicit stack is often a better fix than raising it.

# SECTION 2 - WORKED EXAMPLES
def walk(node):
    yield node["name"]
    for child in node.get("children", []):
        yield from walk(child)

def example_tree():
    catalog = {"name": "Library", "children": [
        {"name": "Rush", "children": [{"name": "Signals"}]}, {"name": "Yes"}]}
    print(list(walk(catalog)))  # => ['Library', 'Rush', 'Signals', 'Yes']

# example_tree()

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Write an iterative traversal with a stack preserving this order.
# ANSWER / CODE: ______________________________________________
# 2. Add cycle detection for a graph of nodes with ids.
# ANSWER / CODE: ______________________________________________
# 3. State time O(nodes) and extra stack space O(depth) for a valid tree.
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: Recursive traversal needs a terminating structure and a depth policy.

# ============================================================
# END OF LESSON
# ============================================================
