# Arguments with Decorators — Study Summary
# Instructor summary:
# - Calling a decorated function actually calls the wrapper bound to its name.
# - The wrapper must accept the arguments that callers supply.
# - def inner(*args, **kwargs): collects positional arguments into a tuple and
#   keyword arguments into a dictionary.
# - fn(*args, **kwargs) unpacks those collections when calling the original function.
# - The same stars collect in a DEFINITION and unpack in a CALL.
# - This lets one decorator wrap functions with different parameter lists.
# - Positional, keyword, and mixed calls can all be forwarded this way.
#
# Clarifications and connections:
# - args and kwargs are conventional names; the stars provide the behavior.
# - Accepting arguments is not enough: the wrapper must also forward them.
# - The original function still enforces its own parameter rules. Forwarding
#   does not make missing, duplicate, or unexpected arguments valid.
# - Arguments are not automatically converted between positional and keyword
#   forms. The wrapper collects them in the form used by its caller.
# - Preserve the original return value by saving fn's result and returning it
#   after any extra behavior. The examples below include that improvement.
# - This lesson concerns arguments to the decorated function, not decorator
#   configuration syntax such as @decorator(option=True).
# - Code after fn(...) runs only if the call returns normally.
# - functools.wraps can preserve metadata; this lesson focuses on forwarding.


# --- 1. Collect and forward arguments in a wrapper ---
def be_nice(fn):
    def inner(*args, **kwargs):
        print("Nice to meet you. I am honored to execute your function for you.")
        result = fn(*args, **kwargs)
        print("It was my pleasure executing your function. Have a nice day.")
        return result

    return inner


@be_nice
def complex_business_logic(stakeholder, position):
    print(f"Something complex for our {position} {stakeholder}.")


complex_business_logic("Boris", "CEO")
# Expected:
# Nice to meet you. I am honored to execute your function for you.
# Something complex for our CEO Boris.
# It was my pleasure executing your function. Have a nice day.
#
# Inside inner, args is ('Boris', 'CEO') and kwargs is {}.
# fn(*args, **kwargs) calls the original function as fn("Boris", "CEO").


# --- 2. Forward keyword and mixed calls ---
complex_business_logic(stakeholder="Boris", position="CEO")
# Same three output lines as section 1.
# args is (); kwargs is {'stakeholder': 'Boris', 'position': 'CEO'}.

complex_business_logic("Boris", position="CEO")
# Same three output lines again.
# args is ('Boris',); kwargs is {'position': 'CEO'}.
# The comma in ('Boris',) identifies a one-element tuple.


# --- 3. Inspect collection and unpacking directly ---
def trace_arguments(fn):
    def wrapper(*args, **kwargs):
        print(args)
        print(kwargs)
        return fn(*args, **kwargs)

    return wrapper


@trace_arguments
def describe_person(name, role):
    return f"{name}: {role}"


print(describe_person("Kevin", role="Developer"))
# Expected:
# ('Kevin',)
# {'role': 'Developer'}
# Kevin: Developer
#
# The wrapper prints its collections, then unpacks them into the original call.
# Passing fn(args, kwargs) instead would pass two whole collection objects as
# positional arguments, which is a different call with different meanings.


# --- 4. Preserve a return value from a different function ---
@be_nice
def add(a, b):
    return a + b


print(add(3, b=5))
# Expected:
# Nice to meet you. I am honored to execute your function for you.
# It was my pleasure executing your function. Have a nice day.
# 8
# The same decorator works with different parameter names and a returned number.
# The wrapper's return passes 8 back to the outer print call.


# --- 5. Defaults are supplied by the original function ---
@trace_arguments
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"


print(greet("Kevin"))
# Expected:
# ('Kevin',)
# {}
# Hello, Kevin!
#
# The wrapper receives no greeting argument. After forwarding, the original
# function uses its own default value. Defaults are not inserted into kwargs.


# --- 6. Forwarding works with zero arguments too ---
@be_nice
def announce_ready():
    return "Ready"


print(announce_ready())
# Expected:
# Nice to meet you. I am honored to execute your function for you.
# It was my pleasure executing your function. Have a nice day.
# Ready
# The wrapper collects () and {}, then calls the original function with no arguments.


# --- 7. The original parameter requirements still apply ---
# Leave these intentional errors commented out:
# complex_business_logic("Boris")
# TypeError: the original function is missing position.
#
# complex_business_logic("Boris", "CEO", hello=True)
# TypeError: the original function does not accept the hello keyword.
#
# complex_business_logic("Boris", stakeholder="Kevin", position="CEO")
# TypeError: the original function receives stakeholder twice.
#
# In each case, inner accepts the supplied arguments and prints its first message.
# The forwarded call then fails, so the final courtesy message does not execute.


# --- 8. Diagnose wrappers that lose arguments ---
# A zero-argument wrapper rejects the caller's arguments before its body runs:
# def no_arguments(fn):
#     def wrapper():
#         return fn()
#     return wrapper
#
# A wrapper that collects but does not forward arguments fails later:
# def forget_to_forward(fn):
#     def wrapper(*args, **kwargs):
#         return fn()
#     return wrapper
#
# With a required-argument original function, the second wrapper accepts the
# caller's values but never supplies them to fn. Correct that call to:
# return fn(*args, **kwargs)
# *args collects positional arguments into a tuple.
# **kwargs collects keyword arguments into a dictionary.
# fn(*args, **kwargs) unpacks and forwards those arguments to the original function.
print("-" * 65)
def announce(fn):
    def wrapper(*args, **kwargs):
        print("Starting")
        result = fn(*args, **kwargs)
        print("Finished")
        return result

    return wrapper


@announce
def album_info(title, artist="Unknown"):
    return f"{title} by {artist}"


print(album_info("Fragile", artist="Yes"))
# Starting
# Finished
# Fragile by Yes
# print("Starting") executes inside the wrapper.
# fn(*args, **kwargs) calls album_info() and stores its returned string in result.
# print("Finished") executes.
# The wrapper returns result, and the outer print() displays "Fragile by Yes".


# --- 9. Practice: predict, explain, then run ---
# Write predictions in ANSWER comments before uncommenting each exercise.
# Keep intentional-error calls commented out.
# Distinguish the wrapper's arguments from the original function's parameters.

# Exercise 1 — Positional arguments
# Predict all three output lines, including the tuple and dictionary.
print(describe_person("Alex", "Designer"))
# Explain how *args forwards the two values.
# ANSWER:
# ('Alex', 'Designer')
# {}
# Alex: Designer
print("-" * 65)
# Exercise 2 — Keyword arguments
# Predict all three output lines. Preserve keyword insertion order in the dict.
print(describe_person(role="Designer", name="Alex"))
# Explain why the original parameters receive the correct values despite this order.
# ANSWER:
# ()
# {'role': 'Designer', 'name': 'Alex'}
# Alex: Designer
# Because both arguments are supplied by keyword, the decorator receives
# Notice that kwargs preserves the order in which you supplied the keywords: role first, then name
print(describe_person("Alex", role="Designer"))
# The wrapper receives "Alex" in the args tuple and "Designer" in the kwargs dictionary. 
# Then fn(*args, **kwargs) forwards both to the original function.
def inspect_args(fn):
    def wrapper(*args, **kwargs):
        print(f"args: {args}")
        print(f"kwargs: {kwargs}")
        return fn(*args, **kwargs)

    return wrapper


@inspect_args
def describe_person(name, role="Unknown"):
    return f"{name}: {role}"


print(describe_person("Alex"))
# args: ('Alex',)
# kwargs: {}
# Alex: Unknown
# The wrapper receives args = ("Alex",) and kwargs = {}.
# The wrapper forwards those arguments using fn(*args, **kwargs).
# Python binds "Alex" to name and uses the default "Unknown" for role.
# The original function returns "Alex: Unknown".
print("-" * 65)
@inspect_args
def describe_person(name, role="Unknown"):
    return f"{name}: {role}"

# print(describe_person("Alex", "Engineer", role="Designer"))
# Python attempts to assign:
# - name = "Alex" — valid.
# - role = "Engineer" — valid positional argument.
# - role = "Designer" — invalid because role already has a value.

print("-" * 65)
# Exercise 3 — Mixed arguments and defaults
# Predict all three output lines for each call.
print(greet("Kevin", greeting="Welcome"))
print(greet(name="Kevin"))
# Explain which call uses the original function's default greeting.
# ANSWER:


# Exercise 4 — Missing forwarding
# Correct the wrapper so the original function receives all caller arguments.
def announce(fn):
    def wrapper(*args, **kwargs):
        print("Calling")
        return fn(*args, **kwargs)
    return wrapper
# Explain why accepting *args and **kwargs alone does not solve the problem.
# ANSWER:
@announce
def show_album(title, artist):
    return f"{title} by {artist}"

print(show_album("Hemispheres", artist="Rush"))

# Exercise 5 — Unexpected keyword
# Explain why this call raises TypeError even though the wrapper accepts **kwargs.
# describe_person("Kevin", "Developer", year=2026)
# Which function rejects year: the wrapper or the original describe_person?
# Keep the failing call commented out.
# ANSWER:
# The wrapper accepts year through **kwargs.
# However, the original describe_person function
# only defines name and role parameters.
# When year is forwarded, Python raises TypeError
# because year is an unexpected keyword argument.

# Exercise 6 — Write your own forwarding decorator
# Write your code below:
# 1. Define announce_result(fn) with a wrapper accepting *args and **kwargs.
def announce_result(fn):
    def wrapper(*args, **kwargs):
        print("Starting")
        
        result =  fn(*args, **kwargs)
        print("Finished")
        return result
    return wrapper

@announce_result
def multiply(a, b):
    return a * b 

# 2. Print "Starting", forward all arguments to fn, and save its result.
# 3. Print "Finished", then return the saved result.
# 4. Return the wrapper from the decorator without calling it.
# 5. Decorate multiply(a, b), which returns a * b.
# 6. Print multiply(6, 7) and multiply(a=6, b=7); predict every output line.
print(multiply(6, 7))
print(multiply(a=6, b=7))

print("-" * 65)
# Optional challenge — Count decorated calls with arguments
# Write your code below:
# Work through this one together when you are ready.
# Define count_calls(fn), with count = 0 in its enclosing scope.
def count_calls(fn):
    count = 0

    def wrapper(*args, **kwargs):
        nonlocal count

        count += 1

        print(f'Call {count}')

        result = fn(*args, **kwargs)

        return result

    return wrapper

@count_calls
def album_label(title, artist, year):
    return f'{title} by {artist} ({year})'
# Its wrapper must accept *args and **kwargs, increment count using nonlocal,
# print "Call {count}", and forward all arguments to fn.
# Return fn's result from the wrapper and return the wrapper from count_calls.
# Decorate album_label(title, artist, year), which returns a formatted label:
# "Hemispheres by Rush (1978)".

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

print(album_label("Hemispheres", "Rush", 1978))
print(album_label(**albums[1]))
print(album_label(**albums[2]))
# Call it once with positional arguments, once with keyword arguments, and once
# with a mixture. Print each returned label and predict the complete output.
# Finally, create an album dictionary and call album_label(**album).
# Explain how **album unpacks at the call site, **kwargs collects in the wrapper,
# and **kwargs unpacks again when forwarding to the original function.
# Assume valid arguments. The counter counts attempted wrapper calls because
# it increments before the original function executes.

# Call 1
# Hemispheres by Rush (1978)
album_label2 = count_calls(album_label)

print(album_label2(**albums[0]))
print(album_label2(**albums[1]))