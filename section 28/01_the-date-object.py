# ============================================================
# FILE: 01_the-date-object.py
# TOPIC: Calendar Dates with datetime.date
# ============================================================
# LESSON OBJECTIVES
# 1. Create a date from a year, month, and day.
# 2. Read date attributes and obtain today's local date.
# 3. Compare dates and create modified copies.
# 4. Convert between dates and ISO date strings.
#
# Run examples separately by uncommenting their function calls.
# Predict results before running. Leave intentional errors commented out.

from datetime import date


# ============================================================
# SECTION 1 — WHAT DOES A date REPRESENT?
# ============================================================
# A date stores a calendar year, month, and day, with no time of day
# or time zone. datetime is the module; date is a class inside it.
# The constructor order is date(year, month, day).
# Use integers, not strings. Years range from 1 through 9999.

def example_create_date():
    birthday = date(2000, 7, 15)
    print(birthday)        # => 2000-07-15
    print(type(birthday)) # => <class 'datetime.date'>
    print(birthday.year)  # => 2000
    print(birthday.month) # => 7
    print(birthday.day)   # => 15


# example_create_date()
# EXERCISE 1 — CREATE
# Create a date for December 31, 2026, and print its month.
# Write your code here:


# ============================================================
# SECTION 2 — TODAY'S LOCAL DATE
# ============================================================
def example_today():
    today = date.today()
    print(today)
    print(today.year)


# example_today()
# The result depends on the computer's local calendar date.
# Use fixed dates when you want repeatable practice results.
# EXERCISE 2 — EXPLAIN
# Why should we avoid a fixed expected output for date.today()?
# ANSWER: ____________________________________________________


# ============================================================
# SECTION 3 — VALID DATES AND LEAP YEARS
# ============================================================
# The constructor validates the entire calendar date.
# Leap years are divisible by 4, except century years must also
# be divisible by 400. Thus 2000 was a leap year; 1900 was not.

def example_invalid_date():
    try:
        impossible = date(2025, 2, 29)
    except ValueError:
        print("That calendar date does not exist.")
    else:
        print(impossible)


# example_invalid_date()
# These raise ValueError; keep them commented out:
# date(2026, 13, 1)
# date(2026, 4, 31)
# EXERCISE 3 — PREDICT
# Which succeeds: date(2024, 2, 29) or date(2023, 2, 29)?
# ANSWER: ____________________________________________________


# ============================================================
# SECTION 4 — WEEKDAYS HAVE TWO NUMBERING SYSTEMS
# ============================================================
def example_weekdays():
    monday = date(2026, 10, 19)
    print(monday.weekday())    # => 0 (Monday=0, Sunday=6)
    print(monday.isoweekday()) # => 1 (Monday=1, Sunday=7)


# example_weekdays()
# EXERCISE 4 — PREDICT
# What does each method return for Sunday?
# weekday(): __________  isoweekday(): __________


# ============================================================
# SECTION 5 — COMPARISONS AND IMMUTABILITY
# ============================================================
# Dates compare chronologically. They are immutable: their stored
# fields cannot be assigned new values. replace() returns a new date.

def example_compare_and_replace():
    original = date(2026, 1, 15)
    revised = original.replace(month=6)
    print(original)             # => 2026-01-15
    print(revised)              # => 2026-06-15
    print(original < revised)   # => True
    print(original == revised)  # => False


# example_compare_and_replace()
# replace() also validates the result: replacing February 29's
# year with a non-leap year raises ValueError.
# EXERCISE 5 — EXPLAIN
# Why doesn't original change when replace() is called?
# ANSWER: ____________________________________________________


# ============================================================
# SECTION 6 — ISO STRINGS: YYYY-MM-DD
# ============================================================
def example_iso_dates():
    original = date(2026, 10, 20)
    text = original.isoformat()
    restored = date.fromisoformat(text)
    print(text)                  # => 2026-10-20
    print(type(text))            # => <class 'str'>
    print(restored == original)  # => True


# example_iso_dates()
# isoformat() produces text; fromisoformat() creates a date.
# Invalid date strings raise ValueError.
# Custom display formats are covered in the strftime lesson.


# ============================================================
# SECTION 7 — CODING CHALLENGES
# ============================================================
# CHALLENGE 1: Write is_weekend(day).
# Accept a date and return True for Saturday or Sunday, else False.
# Test with date(2026, 10, 19) and date(2026, 10, 25).
# Write your code here:


# CHALLENGE 2: Write describe_date(text).
# Parse a YYYY-MM-DD string with date.fromisoformat().
# Catch ValueError and print "Invalid date".
# Otherwise print its year, month, day, and weekday number.
# Test with "2024-02-29", "2025-02-29", and "hello".
# Write your code here:


# ============================================================
# SECTION 8 — FINAL REVIEW
# ============================================================
# 1. What three values does a date store? ______________________
# 2. Does a date store hours or a time zone? ___________________
# 3. Which method returns today's local date? _________________
# 4. What exception signals an impossible calendar date? _______
# 5. Which weekday method numbers Monday as 1? ________________
# 6. Does replace() modify the original date? _________________
# 7. What type does isoformat() return? _______________________
# 8. What type does date.fromisoformat() return? _______________
#
# KEY TAKEAWAY:
# Use date for validated calendar values, comparisons, and dates
# without a time of day. Keep date objects separate from display text.
# ============================================================
# END OF LESSON
# ============================================================
