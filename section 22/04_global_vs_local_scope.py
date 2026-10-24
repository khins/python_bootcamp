# Global vs. Local Scope — Study Summary
# Instructor summary:
# - Scope describes where a name can be resolved in a program.
# - Names assigned at module level belong to that module's global namespace.
# - Parameters and names assigned inside a function are normally local to it.
# - A function can read a global name when no nearer binding shadows it.
# - Calling a function does not make its local names available globally.
# - A local name can shadow a global name without changing the global binding.
# - Module-level constants let several functions share one named value.
# - Write constant names in uppercase, such as TAX_RATE, to express intent.
#
# Clarifications and corrections:
# - Global means module-level, not automatically available across every file.
# - For ordinary function bodies, name lookup follows local, enclosing function,
#   global, then built-in scopes (LEGB). Nested functions add the enclosing step.
# - Assignment anywhere in a function normally makes that name local throughout
#   the function, unless declared global or nonlocal. Reading it before its local
#   value is assigned can therefore raise UnboundLocalError.
# - Reading a global requires no global statement. Rebinding it from inside a
#   function requires global; returning a result is often a clearer design.
# - Scope governs names, not immediate object destruction. Returned objects and
#   values retained by closures can survive the function call that created them.
# - Uppercase names are a convention, not enforced immutability.
# - A global read in a function body uses its current value when executed.
#   Default argument expressions are instead evaluated when the def executes.
# - The tax and tip calculations below are fictional arithmetic examples, not
#   claims about actual tax rates or a universal relationship between tax and tips.


# --- 1. A local name stays local ---
age = 28


def fancy_func():
    nonsense = 10
    return nonsense


print(fancy_func())  # 10
# print(nonsense)  # Intentional NameError: no global name nonsense exists
# The returned integer is available to the caller, but the local name is not.


# --- 2. Read a global from inside a function ---
def show_global_age():
    print(age)


show_global_age()  # 28
# No local age is assigned in this function, so lookup reaches the module's age.


# --- 3. Shadow a global with a separate local binding ---
def show_local_age():
    age = 100
    print(age)


show_local_age()  # 100
print(age)  # 28
# The local assignment does not reassign the module-level age.
# Parameters can also shadow names from an outer scope:


def show_parameter(age):
    print(age)


show_parameter(45)  # 45
print(age)  # 28


# --- 4. Share module-level constants across functions ---
TAX_RATE = 0.06
TIP_TAX_MULTIPLIER = 3


def calculate_tax(price):
    return round(price * TAX_RATE, 2)


def calculate_tip(price):
    return round(price * TAX_RATE * TIP_TAX_MULTIPLIER, 2)


print(calculate_tax(10))  # 0.6
print(calculate_tip(10))  # 1.8
print(f"{calculate_tax(10):.2f}")  # 0.60
print(f"{calculate_tip(10):.2f}")  # 1.80
# Both functions read TAX_RATE from the module namespace.
# This lesson follows the instructor's fictional three-times-tax tip formula.
# round() rounds a number; :.2f formats a string with exactly two decimal places.


# --- 5. A local assignment changes how the whole function resolves a name ---
def broken_age_lookup():
    print(age)
    age = 100


# broken_age_lookup()  # Intentional UnboundLocalError; keep commented out.
# Python treats age as local because this function assigns to it. The earlier
# print cannot read that local yet and does not fall back to the global age.
# UnboundLocalError is a subclass of NameError.
# Use a distinct local name when the intention is to read the global first:


def show_age_comparison():
    local_age = 100
    print(age, local_age)


show_age_comparison()  # 28 100


# --- 6. Return a value without changing a global ---
def next_age(current_age):
    return current_age + 1


updated_age = next_age(age)
print(updated_age)  # 29
print(age)  # 28
# The caller decides whether to save the returned result under a new name or
# explicitly reassign an existing name. The function only uses its parameter.


# --- 7. Default arguments and global reads happen at different times ---
default_volume = 5


def volume_from_body():
    return default_volume


def volume_from_default(volume=default_volume):
    return volume


default_volume = 9
print(volume_from_body())  # 9
print(volume_from_default())  # 5
print(volume_from_default(default_volume))  # 9
# The default value 5 was evaluated when volume_from_default was defined.
# Reassigning default_volume later does not replace that stored default.
# The body lookup and explicit argument above use the current global value, 9.


# --- 8. Practice: predict, explain, then run ---
# Write predictions in ANSWER comments before uncommenting each exercise.
# Keep intentional-error calls commented out.
# Distinguish a local binding from a returned value and from a global binding.

# Exercise 1 — Read the global
# Predict the output and explain where artist is found.
artist = "Rush"
def show_artist():
    print(artist)
show_artist()
# ANSWER:
# Rush 
# artist is global scope or scope outside of the func


# Exercise 2 — Shadow a name
# Predict both outputs. Does the local assignment change the global title?
title = "Hemispheres"
def show_title():
    title = "Tarkus"
    print(title)
show_title()
print(title)
# ANSWER:
# Tarkus
# Hemispheres
# the local assignment does not change global 

# Exercise 3 — A parameter is local
# Predict both outputs and explain what supplies each value.
year = 1978
def show_year(year):
    print(year)
show_year(1981)
print(year)
# ANSWER:
# 1981
# 1978
# year 1981 was supplied to the func and the print has year 1978 as global
# Key takeaway: Function parameters are local variables. Giving a parameter the same name as
# a global variable does not change the global variable.

# Exercise 4 — A returned value is not a global name
# Explain which print succeeds and which raises NameError in this example.
def count_tracks():
    track_count = 4
    return track_count
saved_count = count_tracks()
print(saved_count)
# print(track_count)  # Intentional NameError; keep commented out.
# ANSWER:
# 4 

# Exercise 5 — Read before a local assignment
# Explain why calling this function raises UnboundLocalError instead of printing 10.
score = 10
# def show_score():
#     print(score) # cannot access local variable 'score'
#     score = 20
# show_score()  # Intentional error; keep commented out.
# print(show_score())
# Rewrite the function with a different local name so it can print the global
# score and the local value without changing the global.
# ANSWER:
def show_score():
    new_score = 20
    print(score)
    print(new_score)

show_score()
print(score)

# Exercise 6 — Write functions that share a constant
# Write your code below:
# 1. Define a module-level constant MINUTES_PER_HOUR = 60.
MINUTES_PER_HOUR = 60 
# 2. Define hours_to_minutes(hours) using that constant.
def hours_to_minutes(hours):
    return hours * MINUTES_PER_HOUR

# 3. Define minutes_to_hours(minutes) using the same constant.
def minutes_to_hours(minutes):
    return minutes / MINUTES_PER_HOUR

# 4. Print the results for 2 hours and 90 minutes; predict both outputs.
print(hours_to_minutes(2))
print(minutes_to_hours(90))
# 5. Explain which names are global and which are function parameters.
# 6. Explain whether uppercase spelling prevents reassignment in Python.
# 120
# 1.5
# MINUTES_PER_HOUR is global and hours and minutes are function parameters
#  uppercase spelling does not prevent reassignment


# Optional challenge — Build album labels using a shared separator
# Write your code below:
# Work through this one together when you are ready.
# Define a module-level constant LABEL_SEPARATOR = " | ".
LABEL_SEPARATOR = " | "
# Define album_label(album) to return the title, artist, and year separated by
# that constant, for example "Hemispheres | Rush | 1978".
def album_label(album) -> str:
    # Read LABEL_SEPARATOR inside the function body rather than using a default argument.
    return f'{album["title"]}{LABEL_SEPARATOR}{album["artist"]}{LABEL_SEPARATOR}{album["year"]}'

# Define build_labels(albums) to call album_label for each dictionary and return
# a NEW list of strings in the same order. An empty albums list returns [].
# Keep the result list local, and do not modify the input list or its dictionaries.
# We want this function to:
# 1. Create a new empty list named results.
# 2. Loop through each dictionary in albums.
# 3. Call your existing album_label() function for each dictionary.
# 4. Append each returned string to results.
# 5. Return results after the loop finishes.
def build_labels(albums) -> list:
    result = []
    for album in albums:
        result.append(album_label(album))

    return result

albums = [
    {
        "title": "Moving Pictures",
        "artist": "Rush",
        "year": 1981,
    },
    {
        "title": "Fragile",
        "artist": "Yes",
        "year": 1971,
    },
    {
        "title": "The Dark Side of the Moon",
        "artist": "Pink Floyd",
        "year": 1973,
    },
    {
        "title": "Led Zeppelin IV",
        "artist": "Led Zeppelin",
        "year": 1971,
    },
    {
        "title": "Master of Reality",
        "artist": "Black Sabbath",
        "year": 1971,
    },
]

# Print the returned labels for three albums outside the functions.
labels = build_labels(albums)
print(labels)
print(len(albums))
print(len(labels))

# Explain which names are global, which are local, and why the caller can use
# the returned list without gaining access to build_labels' local variable name.

