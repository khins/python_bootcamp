# ============================================================
# FILE: 01_separate-application-layers.py
# TOPIC: Separate UI, Business Rules, and Storage
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call at a time.
# Expected results appear beside examples. Timing/order may vary where noted.
# Complete the practice yourself; example solutions are separate from practice.
# See learning-guide.txt for section order, setup, and project instructions.

# LESSON OBJECTIVES
# 1. Identify responsibilities.
# 2. Keep pure logic easy to test.

# SECTION 1 - UNDERSTAND THE IDEA
# The companion music-catalog project has core.py for validation and labels,
# storage.py for JSON I/O, and cli.py for arguments/output. UI code translates
# errors to exit status. Business rules need neither a terminal nor a file.
# Avoid a single function that parses arguments, validates, writes, and prints.

# SECTION 2 - WORKED EXAMPLES
def album_label(record):
    return f"{record['title']} by {record['artist']}"

def example_pure_core():
    print(album_label({"title": "Signals", "artist": "Rush"}))
    # => Signals by Rush

# example_pure_core()

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Mark UI, business, and storage lines in an earlier project.
# ANSWER / CODE: ______________________________________________
# 2. Extract one pure helper and test it with an ordinary dictionary.
# ANSWER / CODE: ______________________________________________
# 3. Explain which layer should choose an exit code.
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: Separate responsibilities so each part has a small testable contract.

# ============================================================
# END OF LESSON
# ============================================================
