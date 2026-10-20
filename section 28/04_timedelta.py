# ============================================================
# FILE: 04_timedelta.py
# TOPIC: Durations and Arithmetic with datetime.timedelta
# ============================================================
# LESSON OBJECTIVES
# 1. Create durations using timedelta.
# 2. Add and subtract durations from dates and datetimes.
# 3. Find the difference between two dates or datetimes.
# 4. Distinguish stored components from total duration.
#
# Uncomment individual example calls after predicting the output.

from datetime import date, datetime, timedelta


# ============================================================
# SECTION 1 — A DURATION, NOT A CLOCK READING
# ============================================================
# timedelta represents a duration or difference between dates/times.
# Constructor keywords include weeks, days, hours, minutes, seconds,
# milliseconds, and microseconds. Each defaults to zero.
# Keyword arguments make the intended units easy to read.

def example_create_duration():
    duration = timedelta(days=2, hours=3, minutes=15)
    print(duration)                 # => 2 days, 3:15:00
    print(timedelta(weeks=1))        # => 7 days, 0:00:00
    print(timedelta(minutes=90))     # => 1:30:00
    print(timedelta())              # => 0:00:00


# example_create_duration()
# EXERCISE 1 — CREATE
# Create a duration of 2 weeks, 1 day, and 6 hours.
# Write your code here:


# ============================================================
# SECTION 2 — ADD AND SUBTRACT CALENDAR DAYS
# ============================================================
def example_date_arithmetic():
    start = date(2026, 1, 30)
    print(start + timedelta(days=5))  # => 2026-02-04
    print(start - timedelta(days=7))  # => 2026-01-23
    print(start)                      # => 2026-01-30


# example_date_arithmetic()
# Arithmetic returns a new object and handles month/year boundaries.
# With date objects, only the timedelta's normalized days component
# participates; seconds and microseconds are ignored.
# Use whole-day durations with date and datetime for sub-day arithmetic.
# EXERCISE 2 — PREDICT
# date(2024, 2, 28) + timedelta(days=2)
# ANSWER: ____________________________________________________


# ============================================================
# SECTION 3 — CROSS MIDNIGHT WITH datetime
# ============================================================
def example_datetime_arithmetic():
    start = datetime(2026, 10, 20, 23, 30)
    end = start + timedelta(hours=2)
    print(end)          # => 2026-10-21 01:30:00
    print(end - start)  # => 2:00:00


# example_datetime_arithmetic()
# A time object alone does not support this addition or subtraction.
# These examples use naive datetimes. Time-zone changes and daylight
# saving transitions require additional care outside this lesson.
# EXERCISE 3 — PREDICT
# What is datetime(2026, 12, 31, 23, 45) + timedelta(minutes=30)?
# ANSWER: ____________________________________________________


# ============================================================
# SECTION 4 — SUBTRACTION PRODUCES A timedelta
# ============================================================
def example_date_difference():
    start = date(2026, 10, 20)
    deadline = date(2026, 11, 3)
    remaining = deadline - start
    print(remaining)        # => 14 days, 0:00:00
    print(remaining.days)   # => 14
    print(start - deadline) # => -14 days, 0:00:00


# example_date_difference()
# Subtraction order controls the sign: later - earlier is positive.
# Use matching types: date - date or datetime - datetime.
# EXERCISE 4 — EXPLAIN
# What does a negative result mean when calculating deadline - today?
# ANSWER: ____________________________________________________


# ============================================================
# SECTION 5 — COMPONENTS VERSUS total_seconds()
# ============================================================
# Internally, timedelta normalizes durations into just three fields:
# days, seconds (0–86399), and microseconds (0–999999).
# It has no .hours or .minutes attribute.

def example_duration_components():
    duration = timedelta(days=2, hours=3, minutes=15)
    print(duration.days)             # => 2
    print(duration.seconds)          # => 11700
    print(duration.microseconds)     # => 0
    print(duration.total_seconds())  # => 184500.0
    print(duration.total_seconds() / 3600) # => 51.25


# example_duration_components()
# .seconds is only the seconds remaining after whole days.
# total_seconds() includes all days and fractional seconds.
# EXERCISE 5 — PREDICT
# For timedelta(days=1, seconds=30), what are:
# .seconds? __________  .total_seconds()? __________


# ============================================================
# SECTION 6 — NEGATIVE DURATIONS ARE NORMALIZED TOO
# ============================================================
def example_negative_duration():
    duration = timedelta(hours=-1)
    print(duration)                 # => -1 day, 23:00:00
    print(duration.days)            # => -1
    print(duration.seconds)         # => 82800
    print(duration.total_seconds()) # => -3600.0


# example_negative_duration()
# -1 day + 23 hours equals -1 hour. The positive seconds component
# does not mean the overall duration is positive.
# EXERCISE 6 — EXPLAIN
# Why is total_seconds() safer than .seconds for total elapsed time?
# ANSWER: ____________________________________________________


# ============================================================
# SECTION 7 — COMPARE AND SCALE DURATIONS
# ============================================================
def example_duration_math():
    session = timedelta(minutes=45)
    print(session * 3)                        # => 2:15:00
    print(session / 2)                        # => 0:22:30
    print(session + timedelta(minutes=15))    # => 1:00:00
    print(session < timedelta(hours=1))       # => True
    print(session / timedelta(minutes=15))   # => 3.0


# example_duration_math()
# Dividing by a number returns a duration; dividing by another
# duration returns a numeric ratio.
# timedelta objects are immutable, like date and time objects.


# ============================================================
# SECTION 8 — DAYS ARE NOT CALENDAR MONTHS
# ============================================================
# timedelta has no months= or years= arguments because those units
# do not have a fixed number of days. Four weeks is exactly 28 days,
# which is not the same as advancing one calendar month.
# Adding 365 days is not a general solution for "same date next year".
# Calendar-month/year rules need an explicit policy for cases such
# as January 31 or February 29.


# ============================================================
# SECTION 9 — CODING CHALLENGES
# ============================================================
# CHALLENGE 1: Write due_date(checkout, loan_days=14).
# Accept a date and return the date loan_days later.
# Test with date(2026, 12, 25); the default result is 2027-01-08.
# Write your code here:


# CHALLENGE 2: Write elapsed_minutes(start, end).
# Accept two naive datetimes and return their difference in minutes.
# Use total_seconds() so intervals longer than one day work correctly.
# Test a 90-minute interval and a 1-day-plus-30-minute interval.
# Write your code here:


# CHALLENGE 3: Build three reminder datetimes.
# Starting from datetime(2026, 10, 20, 9), schedule reminders at
# 0, 30, and 60 minutes using a loop and timedelta.
# Format each reminder with "%Y-%m-%d %H:%M" from the prior lesson.
# Write your code here:


# ============================================================
# SECTION 10 — FINAL REVIEW
# ============================================================
# 1. Does timedelta represent a date or duration? ______________
# 2. What type results from subtracting two dates? _____________
# 3. What type results from datetime + timedelta? ______________
# 4. How do .seconds and .total_seconds() differ? ______________
# 5. Can a timedelta be negative? _____________________________
# 6. Why isn't timedelta(days=30) always one calendar month? ____
# 7. Which type should you use for arithmetic across midnight?
# ANSWER: ____________________________________________________
# 8. How do you calculate total duration in hours? _____________
#
# KEY TAKEAWAY:
# Use timedelta for durations and date/datetime arithmetic.
# Use total_seconds() when converting the entire duration to units
# such as minutes or hours, rather than reading only one component.
# ============================================================
# END OF LESSON
# ============================================================
