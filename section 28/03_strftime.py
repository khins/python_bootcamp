# ============================================================
# FILE: 03_strftime.py
# TOPIC: Formatting Dates and Times with strftime
# ============================================================
# LESSON OBJECTIVES
# 1. Turn date and time values into readable strings.
# 2. Build format strings using common percent directives.
# 3. Distinguish formatting from parsing.
# 4. Recognize locale and platform differences in display output.
#
# Uncomment individual example calls after predicting the output.

from datetime import date, datetime, time


# ============================================================
# SECTION 1 — OBJECT IN, FORMATTED STRING OUT
# ============================================================
# strftime() is available on date, time, and datetime objects.
# Its format string mixes literal text with directives beginning with %.
# It returns a string without changing the original object.

def example_format_date():
    day = date(2026, 10, 20)
    label = day.strftime("%Y-%m-%d")
    print(label)        # => 2026-10-20
    print(type(label))  # => <class 'str'>
    print(day.year)     # => 2026


# example_format_date()
# EXERCISE 1 — EXPLAIN
# Does formatting change the stored year, month, or day?
# ANSWER: ____________________________________________________


# ============================================================
# SECTION 2 — COMMON DATE DIRECTIVES
# ============================================================
# %Y  Four-digit year, such as 2026 for our examples.
# %y  Two-digit year, such as 26.
# %m  Month number with zero padding: 01–12.
# %d  Day of month with zero padding: 01–31.
# %A  Full weekday name; %a is the abbreviated name.
# %B  Full month name; %b is the abbreviated name.
# %j  Day of year with zero padding: 001–366.
# %%  A literal percent sign.

def example_date_patterns():
    day = date(2026, 1, 5)
    print(day.strftime("%m/%d/%Y"))      # => 01/05/2026
    print(day.strftime("%d/%m/%Y"))      # => 05/01/2026
    print(day.strftime("Year %Y, day %j")) # => Year 2026, day 005
    print(day.strftime("%A, %B %d, %Y"))
    # In an English locale: Monday, January 05, 2026


# example_date_patterns()
# Names depend on the active locale (language/regional settings).
# Numeric month/day ordering can be ambiguous to readers.
# YYYY-MM-DD is useful when you want an unambiguous date label.
# EXERCISE 2 — PREDICT
# What does date(2026, 7, 4).strftime("%d-%m-%Y") produce?
# ANSWER: ____________________________________________________


# ============================================================
# SECTION 3 — COMMON TIME DIRECTIVES
# ============================================================
# %H  24-hour clock hour: 00–23.
# %I  12-hour clock hour: 01–12 (uppercase i).
# %M  Minute: 00–59. Lowercase %m means MONTH instead.
# %S  Second: 00–59 for the time objects used here.
# %f  Microsecond with six digits.
# %p  Locale's AM/PM equivalent; pair it with %I.

def example_time_patterns():
    clock = time(18, 7, 9, 250000)
    print(clock.strftime("%H:%M:%S"))     # => 18:07:09
    print(clock.strftime("%I:%M %p"))     # => 06:07 PM in English
    print(clock.strftime("%H:%M:%S.%f"))  # => 18:07:09.250000


# example_time_patterns()
# Use date directives with dates and time directives with times.
# Use datetime when you need both sets of fields in one label.
# EXERCISE 3 — FIX THE FORMAT
# A learner uses "%H:%m" to show hours and minutes. Fix it:
# ANSWER: ____________________________________________________


# ============================================================
# SECTION 4 — COMBINE LITERAL TEXT AND DIRECTIVES
# ============================================================
def example_datetime_label():
    meeting = datetime(2026, 10, 20, 14, 5)
    print(meeting.strftime("Meeting: %Y-%m-%d at %H:%M"))
    # => Meeting: 2026-10-20 at 14:05
    print(meeting.strftime("report_%Y%m%d_%H%M.txt"))
    # => report_20261020_1405.txt
    print(meeting.strftime("100%% ready for %Y"))
    # => 100% ready for 2026


# example_datetime_label()
# The filename example only builds a string; it does not create a file.
# Avoid colons in filenames intended for Windows.
# EXERCISE 4 — BUILD
# Format the meeting as "20/10/2026 - 14:05".
# Write your format string here: ______________________________


# ============================================================
# SECTION 5 — strftime FORMATS; strptime PARSES
# ============================================================
# strftime: an object -> a string using a format.
# datetime.strptime: a string + its format -> a datetime.

def example_parse_then_format():
    text = "20/10/2026 14:05"
    parsed = datetime.strptime(text, "%d/%m/%Y %H:%M")
    print(parsed)                        # => 2026-10-20 14:05:00
    print(parsed.strftime("%Y-%m-%d"))  # => 2026-10-20
    print(parsed.date())                 # => 2026-10-20


# example_parse_then_format()
# A string that does not match the format or describes an invalid
# date raises ValueError. Use .date() if you only need the date part.
# EXERCISE 5 — EXPLAIN
# Which method reads "2026-10-20" into an object, and which turns
# an existing object into "October 20, 2026"?
# ANSWER: ____________________________________________________


# ============================================================
# SECTION 6 — PORTABILITY AND DISPLAY CHOICES
# ============================================================
# Names and %p depend on locale. %c, %x, and %X use locale-specific
# date/time, date, and time representations respectively.
# Platform-specific flags such as %-d and %#d are not portable.
# Prefer the common directives above for these exercises.
# To omit leading zeros without those flags, use object attributes:
# day = date(2026, 1, 5)
# print(f"{day.month}/{day.day}/{day.year}")  # => 1/5/2026
#
# Formatting does not convert time zones or change an instant.
# Sorting display strings such as DD/MM/YYYY is not chronological.
# Compare date/datetime objects before formatting for presentation.


# ============================================================
# SECTION 7 — CODING CHALLENGES
# ============================================================
# CHALLENGE 1: Write format_appointment(appointment).
# Accept a datetime and return "YYYY-MM-DD at HH:MM" (24-hour clock).
# Test with datetime(2026, 2, 3, 9, 5).
# Write your code here:


# CHALLENGE 2: Parse "07/04/2026" as month/day/year.
# Print the result as "2026-07-04", then in a format using %B.
# Explain why choosing the correct input order matters.
# Write your code here:


# ============================================================
# SECTION 8 — FINAL REVIEW
# ============================================================
# 1. What type does strftime return? __________________________
# 2. How do %m and %M differ? _________________________________
# 3. How do %H and %I differ? _________________________________
# 4. Which directive displays the full month name? ____________
# 5. How do you include a literal percent sign? ________________
# 6. Which method parses text using a supplied format? _________
# 7. Why might weekday names differ between computers? _________
# 8. Does strftime change the original object? _________________
#
# KEY TAKEAWAY:
# Store and compare date/time objects; format strings for display.
# Choose directives carefully: their capitalization matters.
# ============================================================
# END OF LESSON
# ============================================================
