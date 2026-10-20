# ============================================================
# FILE: 02_the-time-object.py
# TOPIC: Clock Times with datetime.time
# ============================================================
# LESSON OBJECTIVES
# 1. Create a time and read its component attributes.
# 2. Understand defaults, ranges, and microseconds.
# 3. Compare times and create modified copies.
# 4. Distinguish a clock time from a date or duration.
#
# Uncomment individual example calls after predicting the output.

from datetime import date, datetime, time


# ============================================================
# SECTION 1 — A TIME OF DAY, WITHOUT A DATE
# ============================================================
# datetime.time represents a clock reading, not elapsed time.
# It is different from the separate time module used for sleep().
# This lesson uses times without time-zone information (naive times).

def example_create_time():
    opening = time(9, 30, 15)
    print(opening)         # => 09:30:15
    print(opening.hour)    # => 9
    print(opening.minute)  # => 30
    print(opening.second)  # => 15
    print(time())         # => 00:00:00
    print(time(14))       # => 14:00:00


# example_create_time()
# Positional order: hour, minute, second, microsecond.
# All four default to zero. Keyword arguments can improve clarity.
# EXERCISE 1 — CREATE
# Create 6:45 PM using a 24-hour clock.
# Write your code here:


# ============================================================
# SECTION 2 — RANGES AND FRACTIONAL SECONDS
# ============================================================
# hour: 0–23; minute: 0–59; second: 0–59.
# microsecond: 0–999999. One second contains 1,000,000 microseconds.
# These arguments are integers; use microsecond for fractional seconds.

def example_microseconds():
    precise = time(hour=12, minute=5, second=2, microsecond=250000)
    print(precise)              # => 12:05:02.250000
    print(precise.microsecond)  # => 250000


# example_microseconds()
# Invalid components raise ValueError, rather than rolling over:
# time(24, 0)
# time(12, 60)
# EXERCISE 2 — PREDICT
# What fraction of a second is 500000 microseconds? ____________
# Does time(90) represent 90 elapsed hours? ____________________


# ============================================================
# SECTION 3 — COMPARISON AND replace()
# ============================================================
def example_compare_times():
    start = time(9, 30)
    end = time(17, 0)
    revised = start.replace(hour=10)
    print(start < end)   # => True
    print(start)         # => 09:30:00
    print(revised)       # => 10:30:00


# example_compare_times()
# time objects are immutable. replace() returns a new object.
# Comparison orders these naive clock readings within a day.
# Without dates, 01:00 cannot tell you whether it is tomorrow.
# EXERCISE 3 — EXPLAIN
# Why can't comparing time(23) and time(1) establish how long an
# overnight shift lasted?
# ANSWER: ____________________________________________________


# ============================================================
# SECTION 4 — CONVERT TO AND FROM ISO TIME TEXT
# ============================================================
def example_iso_times():
    appointment = time.fromisoformat("14:30:15")
    print(appointment.hour)        # => 14
    print(appointment.isoformat()) # => 14:30:15
    print(type(appointment))       # => <class 'datetime.time'>


# example_iso_times()
# Invalid time strings raise ValueError.
# EXERCISE 4 — PREDICT
# What hour is stored by time.fromisoformat("00:15:00")? _______


# ============================================================
# SECTION 5 — GET THE CURRENT LOCAL TIME
# ============================================================
# time has no today() or now() method. datetime.now() supplies
# a current local date AND time; .time() extracts its clock fields.

def example_current_time():
    current = datetime.now()
    print(current.time())


# example_current_time()
# Output changes when you run it. The resulting time here is naive.
# Time zones are a separate topic: naive values contain no UTC offset.


# ============================================================
# SECTION 6 — COMBINE A DATE AND TIME
# ============================================================
def example_combine():
    day = date(2026, 10, 20)
    clock = time(14, 30)
    appointment = datetime.combine(day, clock)
    print(appointment)         # => 2026-10-20 14:30:00
    print(appointment.date())  # => 2026-10-20
    print(appointment.time())  # => 14:30:00


# example_combine()
# A datetime stores both parts. Use datetime objects for arithmetic
# that needs a calendar day, such as crossing midnight.
# Subtracting two time objects directly raises TypeError.
# Adding a timedelta to a time directly also raises TypeError.


# ============================================================
# SECTION 7 — CODING CHALLENGES
# ============================================================
# CHALLENGE 1: Write is_business_hour(clock).
# Return True from 09:00 inclusive to 17:00 exclusive.
# Assume a naive time and business hours within one day.
# Test 08:59, 09:00, 16:59, and 17:00.
# Write your code here:


# CHALLENGE 2: Create a meeting datetime from a date and a time.
# Print the meeting, then create a new time 30 minutes past the
# same hour using replace(minute=30). Keep the original unchanged.
# Write your code here:


# ============================================================
# SECTION 8 — FINAL REVIEW
# ============================================================
# 1. Does time represent a duration or clock reading? __________
# 2. What does time() represent? ______________________________
# 3. What is the largest valid hour? __________________________
# 4. How many microseconds are in one second? __________________
# 5. Can time represent a date? _______________________________
# 6. How can you extract a time from datetime.now()? ___________
# 7. Which method joins a date and a time? _____________________
# 8. Can you subtract two time objects directly? _______________
#
# KEY TAKEAWAY:
# Use time for a clock reading, datetime for a date plus a clock
# reading, and timedelta for a duration.
# ============================================================
# END OF LESSON
# ============================================================
