# ============================================================
# FILE: 06_album-and-track-project.py
# TOPIC: Project: Model Albums and Tracks
# ============================================================
# STUDY GUIDE
# Python 3.11+. Predict before running; uncomment one example call at a time.
# Expected results appear beside examples. Timing/order may vary where noted.
# Complete the practice yourself; example solutions are separate from practice.
# See learning-guide.txt for section order, setup, and project instructions.

# LESSON OBJECTIVES
# 1. Compose dataclasses and enums.
# 2. Calculate derived values without storing duplicates.

# SECTION 1 - UNDERSTAND THE IDEA
# An album owns a fresh list of tracks; tracks are immutable validated values.
# Compute total_seconds from tracks so it cannot go stale after adding a track.
# The sample durations are synthetic. Type annotations do not enforce the media
# argument at runtime, so callers must validate external values before creation.

# SECTION 2 - WORKED EXAMPLES
from dataclasses import dataclass, field
from enum import Enum

class Media(Enum):
    DIGITAL = "digital"
    CD = "cd"

@dataclass(frozen=True)
class Track:
    title: str
    seconds: int

    def __post_init__(self):
        if not isinstance(self.title, str) or not self.title.strip():
            raise ValueError("title is required")
        if type(self.seconds) is not int or self.seconds < 0:
            raise ValueError("invalid duration")

@dataclass
class Album:
    title: str
    artist: str
    media: Media = Media.DIGITAL
    tracks: list[Track] = field(default_factory=list)

    @property
    def total_seconds(self):
        return sum(track.seconds for track in self.tracks)

def example_catalog():
    album = Album("Demo", "Rush", tracks=[Track("A", 100), Track("B", 200)])
    print(album.total_seconds, album.media.value)  # => 300 digital
    print(Album("Empty", "Yes").total_seconds)     # => 0

# example_catalog()

# ============================================================
# PRACTICE AND FINAL REVIEW
# ============================================================
# 1. Build your own album model with a release year and validated format.
# ANSWER / CODE: ______________________________________________
# 2. Add a track and show that total_seconds changes without manual synchronization.
# ANSWER / CODE: ______________________________________________
# 3. Test two albums to ensure their default track lists are independent.
# ANSWER / CODE: ______________________________________________
# KEY TAKEAWAY: Compose small validated records and derive values from their source data.

# ============================================================
# END OF LESSON
# ============================================================
