# ============================================================
# FILE: 05_build-a-reusable-iterable.py
# TOPIC: Building a Reusable Iterable
# ============================================================
# STUDY GUIDE
# Predict before running. Uncomment individual example calls.
# Expected outputs appear in comments. Complete the exercises yourself.
# All examples use the standard library; no packages need installation.

# LESSON OBJECTIVES
# 1. Separate stored data from traversal state.
# 2. Support independent and nested loops.

# SECTION 1 — FRESH ITERATORS FOR EACH TRAVERSAL
class Playlist:
    def __init__(self, songs):
        self.songs = tuple(songs)

    def __iter__(self):
        return iter(self.songs)


# Unlike Countdown, Playlist is not itself an iterator:
# it has __iter__ but no __next__. The tuple stores the songs.
# Each call to iter(playlist) creates a fresh tuple iterator.
# tuple(songs) eagerly consumes songs; an infinite input is unsuitable.


# SECTION 2 — REPEATED TRAVERSALS
def example_repeatable_playlist():
    playlist = Playlist(["Tom Sawyer", "Limelight"])
    print(list(playlist))  # => ['Tom Sawyer', 'Limelight']
    print(list(playlist))  # => ['Tom Sawyer', 'Limelight']
    first = iter(playlist)
    second = iter(playlist)
    print(next(first))   # => Tom Sawyer
    print(next(first))   # => Limelight
    print(next(second))  # => Tom Sawyer


# example_repeatable_playlist()


# SECTION 3 — NESTED LOOPS NEED INDEPENDENT POSITIONS
def example_nested_loops():
    playlist = Playlist(["A", "B"])
    print([(left, right) for left in playlist for right in playlist])
    # => [('A', 'A'), ('A', 'B'), ('B', 'A'), ('B', 'B')]


# example_nested_loops()
# Avoid storing a single cursor on Playlist and returning it every time.
# That would cause separate loops to interfere with each other's progress.

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Explain why Playlist.__iter__ does not return self.
# ANSWER / CODE: ______________________________________________
# 2. Replace playlist with iter(playlist) in the nested loop and predict it.
# ANSWER / CODE: ______________________________________________
# 3. Design a repeatable collection of three album titles.
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: Reusable collections provide a fresh iterator for each traversal.

# ============================================================
# END OF LESSON
# ============================================================

