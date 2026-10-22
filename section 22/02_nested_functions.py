# Nested Functions — Study Summary
# Instructor summary:
# - A nested function is defined inside the body of another function.
# - Inner functions can organize an outer function into smaller, related steps.
# - Indent the inner definition within the outer function, then indent its
#   own body one level further.
# - Defining a nested function does not execute its body; calling it does.
# - A nested function's name is local to the enclosing function.
# - The outer function can call its helpers and use their returned values.
# - Nested functions help prepare us for closures and decorators.
#
# Clarifications and corrections:
# - A local helper name is not automatically available at module level.
#   However, the function object CAN be returned and called through another name.
# - A nested function can survive its outer call if a reference to it is retained.
# - Each time execution reaches an inner def statement, it creates a function
#   object and binds that object to a local name.
# - An inner return exits that inner call, not the entire outer function.
# - The conversions below use US customary liquid units: 1 gallon = 4 quarts,
#   1 quart = 2 pints, and 1 pint = 2 cups. Thus 1 gallon = 16 cups.
# - Three gallons is 3 * 16 = 48 cups.
# - Nesting can extend beyond one level, but deep nesting reduces readability
#   and practical interpreter limits exist; it is not literally unlimited.


# --- 1. Split a conversion into three nested helpers ---
def convert_gallons_to_cups(gallons):
    def gallons_to_quarts(gallons):
        print(f"Converting {gallons} gallons to quarts!")
        return gallons * 4

    def quarts_to_pints(quarts):
        print(f"Converting {quarts} quarts to pints!")
        return quarts * 2

    def pints_to_cups(pints):
        print(f"Converting {pints} pints to cups!")
        return pints * 2

    quarts = gallons_to_quarts(gallons)
    pints = quarts_to_pints(quarts)
    cups = pints_to_cups(pints)
    return cups


print(convert_gallons_to_cups(1))
# Expected:
# Converting 1 gallons to quarts!
# Converting 4 quarts to pints!
# Converting 8 pints to cups!
# 16

print(convert_gallons_to_cups(3))
# Expected:
# Converting 3 gallons to quarts!
# Converting 12 quarts to pints!
# Converting 24 pints to cups!
# 48
# The three helpers are siblings inside the outer function, not inside each other.
# Their bodies use eight spaces of indentation; the outer steps use four.


# --- 2. Follow arguments and return values ---
# In convert_gallons_to_cups(3):
# 1. The outer gallons parameter receives 3.
# 2. gallons_to_quarts(3) returns 12, assigned to the outer local name quarts.
# 3. quarts_to_pints(12) returns 24, assigned to pints.
# 4. pints_to_cups(24) returns 48, assigned to cups.
# 5. The OUTER return sends 48 back to the original caller.
#
# The inner gallons parameter and outer gallons parameter are separate local
# names. The outer value is explicitly passed into the helper's parameter.
# Each inner return hands control back to the next step of the outer function.


# --- 3. A local helper name is not a global name ---
# Leave these intentional errors commented out:
# print(pints_to_cups(3))  # NameError: no module-level name pints_to_cups
# print(quarts)  # NameError: quarts was local to the conversion function
#
# Calling convert_gallons_to_cups() does not publish its local names globally.
# This is name scope, not a rule preventing function objects from being returned.


# --- 4. A definition alone does not run the helper ---
def demonstrate_definition():
    def announce():
        print("The inner function ran.")

    print("The outer function ran.")


demonstrate_definition()  # The outer function ran.
# announce is defined during this call, but nothing calls announce().
# Adding announce() inside the outer body would run the inner print too.


# --- 5. Return a nested function for later use ---
def make_doubler():
    def double(number):
        return number * 2

    return double


doubler = make_doubler()
print(doubler(5))  # 10
print(type(doubler))  # <class 'function'>
# make_doubler() returns the function object, not the result of calling double.
# The outer call has finished, but doubler still refers to its nested function.
# The name double itself is still not defined at module level.
# print(double(5))  # Intentional NameError; keep commented out.


# --- 6. Keep a calculation separate from demonstration prints ---
def gallons_to_cups_quiet(gallons):
    def gallons_to_quarts(amount):
        return amount * 4

    def quarts_to_pints(amount):
        return amount * 2

    def pints_to_cups(amount):
        return amount * 2

    quarts = gallons_to_quarts(gallons)
    pints = quarts_to_pints(quarts)
    return pints_to_cups(pints)


print(gallons_to_cups_quiet(0))  # 0
print(gallons_to_cups_quiet(0.5))  # 8.0
print(gallons_to_cups_quiet(3))  # 48
# These examples assume numeric inputs representing nonnegative amounts.
# The functions do not enforce that assumption or perform input validation.
# For this simple calculation, gallons * 16 would suffice; the helpers are
# included to practice nested definitions and step-by-step calls.


# --- 7. Practice: predict, explain, then run ---
# Write predictions in ANSWER comments before uncommenting each exercise.
# Distinguish function definitions, function calls, printed output, and returns.
# Keep intentional-error examples commented out.

print('-' * 32)
# Exercise 1 — Trace the conversion
# Predict every printed line in order, including the outer print's output.
print(convert_gallons_to_cups(2))
# State the intermediate quarts and pints values.
# ANSWER:
# 8 quarts
# 16 pints
# 32 cups


# Exercise 2 — Definition versus execution
# Predict the output. Does the inner function run? Explain why.
def outer():
    def inner():
        print("Inside")
    print("Outside")

outer()
# ANSWER:
# Outside

def outer():
    def inner():
        print("Inside")

    print("Outside")
    inner()

outer()
# Key concept: The order in which functions are defined doesn't determine
#  when they execute. The order of function calls does.

# Exercise 3 — Return to the caller
# Predict every output line in order. Explain why "After" still prints.
def outer():
    def inner():
        return 7
    print("Before")
    result = inner()
    print("After")
    return result + 1

print(outer())
# ANSWER:
# Before
# After
# 8

# Exercise 4 — Diagnose the scope
# Explain why the last line raises NameError even after the outer call succeeds.
print(gallons_to_cups_quiet(1))
# print(pints_to_cups(2))  # Intentional NameError; keep commented out.
# Where would a call to that helper by its local name need to appear?
# ANSWER:

def outer():
    def inner():
        return 10

    return inner

selected = outer()
print(selected())
# Here's what happens:
# 1. outer() defines the nested function inner().
# 2. return inner returns a reference to the function, without executing it.
# 3. selected = outer() stores that function reference.
# 4. selected() executes the returned function.
# 5. The function returns 10, which gets printed.
# This is an important foundation for two advanced Python concepts:
# - Higher-order functions: Functions that accept or return other functions.
# - Closures: Inner functions that retain access to variables from their enclosing scope.

# Exercise 5 — A returned helper
# Predict both outputs. Explain what operation holds after the first line.
operation = make_doubler()
print(type(operation))
print(operation(9))
# Does the outer function need to remain running for operation(9) to work?
# ANSWER:
# <class 'function'>
# 18
# the outer function need not to remain running because operation has a reference to the function
# Here's what happens:
# 1. make_doubler() executes.
# 2. Python creates the nested function double().
# 3. return double returns a reference to that function.
# 4. operation now references the returned function.
# 5. operation(9) calls it and returns 18.
# This is an important foundation for understanding closures in Python.

# Exercise 6 — Write your own nested conversion
# Write your code below:
# 1. Define hours_to_seconds(hours).
def hours_to_seconds(hours) -> int:
    # 2. Inside it, define hours_to_minutes(amount), returning amount * 60.
    def hours_to_minutes(amount):
        return amount * 60
    # 3. Also inside it, define minutes_to_seconds(amount), returning amount * 60.
    def minutes_to_seconds(amount):
        return amount * 60
    # 4. Call the helpers in sequence and return the final number of seconds.
    hour_min = hours_to_minutes(hours)
    min_sec = minutes_to_seconds(hour_min)
    return min_sec

# 5. Outside the function, print results for 2, 0, and 0.5 hours.
print(hours_to_seconds(2))
print(hours_to_seconds(0))
print(hours_to_seconds(0.5))

# 6. Predict the outputs and explain why the helpers' names are local.
# The helper function names are local because they are
# defined inside the hours_to_seconds() function.
# They can be called by name within that enclosing function,
# but not directly from outside it.


# Optional challenge — Build an album report with a nested helper
# Write your code below:
# Work through this one together when you are ready.
# Define build_album_report(albums).
def build_album_report(albums) -> list:
    results = []
    # Inside build_album_report, define format_album(album) to return a string such as:
    # "Hemispheres by Rush (1978)"
    # Still inside the outer function, loop over albums and call format_album on
    # each dictionary. Append each returned string to a NEW list, then return it.
    # Preserve album order and leave the input list and dictionaries unchanged.
    def format_album(album):
        return f'{album["title"]} by {album["artist"]} ({album["year"]})'

    for album in albums:
        results.append(format_album(album))

    return results

# albums is a list of dictionaries with "title", "artist", and "year" keys.
albums = [
    {
        "title": "Hemispheres",
        "artist": "Rush",
        "year": 1978,
    },
    {
        "title": "Going for the One",
        "artist": "Yes",
        "year": 1977,
    },
    {
        "title": "Wish You Were Here",
        "artist": "Pink Floyd",
        "year": 1975,
    },
]

print(build_album_report(albums))
print(build_album_report([]))
selected = build_album_report(albums)

print(type(selected))
print(selected(albums[0]))

# An empty input list should return []. Do not print inside either function.
# Test by printing build_album_report's result for three album dictionaries.
# Explain what each function returns and why format_album cannot be called
# directly by that name at module level.

