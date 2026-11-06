# ============================================================
# FILE: 08_listening-history-project.py
# TOPIC: Project: Listening-history Analyzer
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call at a time.
# Expected results appear beside examples. Timing/order may vary where noted.
# Complete the practice yourself; example solutions are separate from practice.
# See learning-guide.txt for section order, setup, and project instructions.

# LESSON OBJECTIVES
# 1. Combine counting, grouping, and bounded history.
# 2. Validate input before aggregating.

# SECTION 1 - UNDERSTAND THE IDEA
# Each record has artist, title, and nonnegative integer seconds. This worked
# version consumes any iterable once and keeps summary state. Album metadata
# is synthetic. Reject bool seconds explicitly because bool subclasses int.
# Recent history is bounded, but per-artist dictionaries grow with artist count.

# SECTION 2 - WORKED EXAMPLES
from collections import Counter, defaultdict, deque

def analyze(records):
    counts = Counter()
    seconds = defaultdict(int)
    recent = deque(maxlen=3)
    for row in records:
        if not isinstance(row, dict):
            raise ValueError("record must be a dictionary")
        artist, title, duration = row.get("artist"), row.get("title"), row.get("seconds")
        if not isinstance(artist, str) or not artist.strip():
            raise ValueError("artist is required")
        if not isinstance(title, str) or not title.strip():
            raise ValueError("title is required")
        if type(duration) is not int or duration < 0:
            raise ValueError("seconds must be a nonnegative integer")
        artist = artist.strip()
        counts[artist] += 1
        seconds[artist] += duration
        recent.append(title.strip())
    return dict(counts), dict(seconds), list(recent)

def example_analyzer():
    rows = [{"artist": "Rush", "title": "YYZ", "seconds": 200},
            {"artist": "Rush", "title": "Limelight", "seconds": 240}]
    print(analyze(iter(rows)))  # => ({'Rush': 2}, {'Rush': 440}, ['YYZ', 'Limelight'])
    print(analyze([]))          # => ({}, {}, [])
    try:
        analyze([{"artist": "Rush", "title": "YYZ", "seconds": -1}])
    except ValueError as error:
        print(error)  # => seconds must be a nonnegative integer

# example_analyzer()

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Build your own version returning the top two artists and average duration.
# ANSWER / CODE: ______________________________________________
# 2. Test empty input, a missing title, and boolean seconds.
# ANSWER / CODE: ______________________________________________
# 3. Add an artist filter using a generator without copying all records.
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: Combine specialized collections around a clear record contract.

# ============================================================
# END OF LESSON
# ============================================================
