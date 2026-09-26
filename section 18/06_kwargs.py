# **kwargs — Study Summary
# Instructor summary:
# - A keyword argument supplies a name and value in a call: word="Hello".
# - **kwargs in a function definition collects extra keyword arguments into a dict.
# - Keyword names become string keys; their supplied values become dictionary values.
# - Keywords matching explicit parameters fill those parameters, not kwargs.
# - With no extra keyword arguments, kwargs is an empty dictionary: {}.
# - *args collects extra positional arguments into a tuple.
# - When using both, *args comes before **kwargs in the function definition.
# - args and kwargs are conventional names; the stars create the behavior.
# - Inside the function, use args and kwargs as ordinary variable names.
# - **kwargs does not collect extra positional arguments or remove requirements
#   for other required parameters.
#
# Precision notes:
# - Parameters such as a and b are not defaults unless given default values.
# - ** can also unpack a mapping in a function CALL; that is a separate use
#   from collecting keyword arguments in a function definition.


# --- 1. Review positional and keyword arguments ---
def word_length(word):
    return len(word)


print(word_length("Hello"))       # 5 — positional argument
print(word_length(word="Hello"))  # 5 — keyword argument

# Leave these intentional errors commented out:
# word_length()  # TypeError — missing the required word argument
# word_length(something="Hello")  # TypeError — unexpected keyword
# word_length(word="Hello", extra=3)  # TypeError — unexpected keyword


# --- 2. Collect arbitrary keyword arguments ---
def collect_keyword_arguments(**kwargs):
    print(kwargs)
    print(type(kwargs))


collect_keyword_arguments(a=2, b=3, c=4)
# Expected:
# {'a': 2, 'b': 3, 'c': 4}
# <class 'dict'>

collect_keyword_arguments()
# Expected:
# {}
# <class 'dict'>
# In the call, write a=2; Python creates the string key 'a' in kwargs.
# kwargs is a dictionary, not a tuple of pairs.


# --- 3. Use dictionary methods inside the function ---
def show_details(**details):
    for key, value in details.items():
        print(f"The key is {key} and the value is {value}.")


show_details(artist="Rush", song="YYZ", year=1981)
# Expected:
# The key is artist and the value is Rush.
# The key is song and the value is YYZ.
# The key is year and the value is 1981.
# **details works just like **kwargs: the chosen name is different.
# The dictionary preserves the order in which keyword arguments were supplied.
# show_details() would print nothing because there would be no entries to visit.


# --- 4. Explicit parameters receive matching arguments first ---
def describe_song(title, **details):
    print(title)
    print(details)




describe_song(title="YYZ", artist="Rush", year=1981)
# Expected:
# YYZ
# {'artist': 'Rush', 'year': 1981}
# title fills the named parameter, so it is not an entry in details.

describe_song("Roundabout")
# Expected:
# Roundabout
# {}

# Leave these intentional errors commented out:
# describe_song(artist="Rush")  # TypeError — title is still required
# describe_song("YYZ", title="Roundabout")  # TypeError — title received two values
# collect_keyword_arguments(2, 3)  # TypeError — this function accepts no positional arguments


# --- 5. Combine regular parameters, *args, and **kwargs ---
def show_argument_groups(a, b, *args, **kwargs):
    print(a, b)
    print(args)
    print(kwargs)


show_argument_groups(1, 2, 3, 4, 5, 6, x=8, y=9, z=10)
# Expected:
# 1 2
# (3, 4, 5, 6)
# {'x': 8, 'y': 9, 'z': 10}
# The first two positional arguments fill a and b.
# The remaining positional arguments form args.
# The extra keyword arguments form kwargs.

show_argument_groups(b=2, a=1, bonus=7)
# Expected:
# 1 2
# ()
# {'bonus': 7}
# a and b can also be supplied by keyword, in either order.


# --- 6. Calculate with each group ---
def argument_totals(a, b, *args, **kwargs):
    # For this example, all supplied arguments must have numeric values.
    print(f"Regular total: {a + b}")
    print(f"Positional extras total: {sum(args)}")

    keyword_total = 0
    for value in kwargs.values():
        keyword_total += value
    print(f"Keyword extras total: {keyword_total}")
    # sum(kwargs.values()) would also calculate the keyword total.


argument_totals(1, 2, 3, 4, 5, 6, x=8, y=9, z=10)
# Expected:
# Regular total: 3
# Positional extras total: 18
# Keyword extras total: 27

argument_totals(1, 2)
# Expected:
# Regular total: 3
# Positional extras total: 0
# Keyword extras total: 0
# Empty collections contribute zero to these totals.
# sum(kwargs) would iterate over its keys, not its numeric values.


# --- 7. Practice: predict, explain, then run ---
# Write predictions in the ANSWER comments before uncommenting each exercise.
# Keep intentional-error calls commented out.
# Distinguish printed output from a function's returned value.

# Exercise 1 — Collect keywords
# Predict both outputs. What type of object is options?
# def collect_options(**options):
#     return options
#
# print(collect_options(volume=9, subtitles=True))
# print(collect_options())
# ANSWER:


# Exercise 2 — Named parameter vs. extra keywords
# Predict all three output lines. Why is name absent from extras?
# def show_profile(name, **extras):
#     print(name)
#     print(extras)
#     print(len(extras))
#
# show_profile(name="Kevin", city="Chicago", hobby="guitar")
# ANSWER:


# Exercise 3 — Separate positional and keyword extras
# Predict all four output lines. State the types of args and kwargs.
# def inspect_arguments(first, *args, **kwargs):
#     print(first)
#     print(args)
#     print(kwargs)
#     print(len(args) + len(kwargs))
#
# inspect_arguments("start", 10, 20, volume=5, mode="demo")
# ANSWER:


# Exercise 4 — Empty collections and keyword binding
# Predict all three outputs. Explain why a and b do not appear in kwargs.
# def inspect_groups(a, b, *args, **kwargs):
#     print(a + b)
#     print(args)
#     print(kwargs)
#
# inspect_groups(b=4, a=3)
# ANSWER:


# Exercise 5 — Diagnose the calls
# For each call, say whether it succeeds or raises TypeError, and explain why.
# For successful calls, predict the returned dictionary.
# Uncomment the function and only the successful calls when checking your work.
# def make_record(title, **details):
#     return details
#
# A: make_record("YYZ", artist="Rush")
# B: make_record(artist="Rush")
# C: make_record("YYZ", "Rush")
# D: make_record("YYZ", title="Roundabout")
# E: make_record(title="YYZ")
# ANSWER:


# Exercise 6 — Write your own keyword summary
# 1. Define show_album(title, **details).
# 2. Print title once, then loop over details.items() to print each key and value.
# 3. After the loop, print the number of extra details received.
# 4. Call it with an album title and artist, year, and genre keyword arguments.
# 5. Call it again with only an album title.
# 6. Predict both calls' output and explain why title is not counted in details.
# Write your code below:


# Optional challenge — Total all three argument groups
# Work through this one together when you are ready.
# Define combined_total(base, *numbers, **extras).
# Assume base, all numbers, and all extras values are integers.
# Return the sum of base, the positional extras, and the keyword extras values.
# Use sum() and values(). Return the result rather than printing inside the function.
# combined_total(10, 2, 3, bonus=4, adjustment=-1) => 18
# combined_total(10) => 10
# combined_total(base=5, bonus=2) => 7
# Explain which arguments fill base, numbers, and extras in the first call.
# Write your code below:
