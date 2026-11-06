# ============================================================
# FILE: 04_serialization-limits.py
# TOPIC: Translate Unsupported Values
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call at a time.
# Expected results appear beside examples. Timing/order may vary where noted.
# Complete the practice yourself; example solutions are separate from practice.
# See learning-guide.txt for section order, setup, and project instructions.

# LESSON OBJECTIVES
# 1. Serialize an enum/dataclass explicitly.
# 2. Avoid assuming JSON preserves all Python types.

# SECTION 1 - UNDERSTAND THE IDEA
# JSON has no native set, datetime, bytes, or arbitrary class instances. Define
# an explicit external representation instead of blindly converting everything
# to str. asdict converts dataclasses recursively, but enum values inside still
# need conversion. allow_nan=False rejects nonstandard NaN/infinity output.

# SECTION 2 - WORKED EXAMPLES
import json
from dataclasses import dataclass
from enum import Enum

class Format(Enum):
    CD = "cd"

@dataclass
class Album:
    title: str
    media: Format

def example_encoding_model():
    album = Album("Signals", Format.CD)
    external = {"title": album.title, "media": album.media.value}
    print(json.dumps(external))  # => {"title": "Signals", "media": "cd"}
    try:
        json.dumps({"seconds": float("nan")}, allow_nan=False)
    except ValueError:
        print("non-finite value rejected")  # => non-finite value rejected

# example_encoding_model()

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Serialize a date with ISO format and reconstruct it.
# ANSWER / CODE: ______________________________________________
# 2. Explain information lost by converting every unknown object to str.
# ANSWER / CODE: ______________________________________________
# 3. Design a version field for a catalog format.
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: Serialization is a deliberate mapping, not a perfect copy of memory.

# ============================================================
# END OF LESSON
# ============================================================
