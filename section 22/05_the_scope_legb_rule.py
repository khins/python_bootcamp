# The LEGB Scope Rule — Study Summary
# Instructor summary:
# - LEGB describes ordinary name lookup in Python function bodies:
#   Local -> Enclosing function scopes -> Global -> Built-in.
# - Python uses the nearest applicable binding of a name.
# - Local names include the current function's parameters and assignments.
# - Enclosing scopes belong to functions surrounding the current definition.
# - Global names belong to the module where the function was defined.
# - Built-in names include len, print, and sum.
# - A name absent from all applicable scopes raises NameError.
# - A function can return a built-in function object without calling it.
#
# Clarifications and corrections:
# - The acronym is LEGB, not "league". B means built-in names, not keywords.
#   Keywords such as if, return, and def are syntax, not names looked up this way.
# - With multiple enclosing functions, lookup proceeds from nearest to farthest.
# - Enclosing scopes follow where a function was defined, not who calls it.
# - A local assignment normally classifies the name as local throughout the
#   function. Reading it before assignment raises UnboundLocalError rather
#   than falling back to an enclosing or global value.
# - global and nonlocal declarations can change how a name is bound; ordinary
#   reads of outer names do not require either declaration.
# - Avoid naming ordinary variables len, list, or sum: they can shadow useful
#   built-ins. Python does not skip a binding just because it is not callable.
# - LEGB is a useful model for ordinary function lookup, not every Python context.
#   Attribute access such as object.name follows different rules.


# --- 1. L: the local binding takes priority ---
x = 15


def outer_local():
    x = 10

    def inner():
        x = 5
        return x

    return inner()


print(outer_local())  # 5
print(x)  # 15
# Inside inner, x refers to its own local 5. The enclosing 10 and global 15
# remain separate bindings. The outer function returns inner's result.


# --- 2. E: use the enclosing function's binding ---
def outer_enclosing():
    x = 10

    def inner():
        return x

    return inner()


print(outer_enclosing())  # 10
# inner has no local x binding, so its lookup reaches outer_enclosing's x.
# That enclosing binding takes priority over the module's x = 15.


# --- 3. G: reach the module's global binding ---
def outer_global():
    def inner():
        return x

    return inner()


print(outer_global())  # 15
# Neither inner nor outer_global binds x, so the module-level binding is used.
# Other functions' local variables are not part of this lookup path.


# --- 4. B: return a built-in function ---
def outer_builtin():
    def inner():
        return len

    return inner()


length_function = outer_builtin()
print(length_function is len)  # True
print(length_function("Python"))  # 6
print(outer_builtin()("Python"))  # 6
# No local, enclosing, or global name len shadows the built-in here.
# inner returns len itself. outer_builtin returns that same function object.
# Only the later call with "Python" calculates the string length.


# --- 5. Search enclosing functions from nearest to farthest ---
def outer_layers():
    label = "outer"

    def middle():
        label = "middle"

        def inner():
            return label

        return inner()

    return middle()


print(outer_layers())  # middle
# inner first finds label in middle, its nearest enclosing function.
# If middle did not bind label, outer_layers' binding would be used.


# --- 6. The caller's locals do not become an enclosing scope ---
def read_global_x():
    return x


def caller():
    x = 99
    return read_global_x()


print(caller())  # 15
# read_global_x was defined at module level, not inside caller.
# It reads the module's x, even when called by a function with its own local x.


# --- 7. A local binding can block fallback ---
def broken_lookup():
    print(x)
    x = 5


# broken_lookup()  # Intentional UnboundLocalError; keep commented out.
# The assignment makes x local throughout broken_lookup. At print(x), that
# local value has not been assigned yet. Python does not use the global 15.


def shadow_builtin():
    len = 99
    return len


print(shadow_builtin())  # 99
print(len("Python"))  # 6 — the local shadow did not replace the built-in
# Trying len("Python") INSIDE shadow_builtin would attempt to call 99 and
# raise TypeError. It would not continue searching for a callable built-in len.


# --- 8. Missing names raise NameError ---
def missing_lookup():
    return nonexistent_scope_example


# missing_lookup()  # Intentional NameError; keep commented out.
# nonexistent_scope_example has no binding in any applicable scope here.
# UnboundLocalError is a more specific kind of NameError for an unbound local.


# --- 9. Practice: predict, explain, then run ---
# Write predictions in ANSWER comments before uncommenting each exercise.
# Identify the LEGB level supplying each name where requested.
# Keep intentional-error calls commented out.

# Exercise 1 — Local wins
# Predict both outputs. Which scope supplies artist inside show_artist?
# artist = "Rush"
# def show_artist():
#     artist = "Yes"
#     return artist
# print(show_artist())
# print(artist)
# ANSWER:


# Exercise 2 — Enclosing beats global
# Predict the output. Which scope supplies title to inner?
# title = "Tarkus"
# def outer():
#     title = "Hemispheres"
#     def inner():
#         return title
#     return inner()
# print(outer())
# ANSWER:


# Exercise 3 — A built-in as a return value
# Predict both outputs. Explain when len is actually called.
# selected = outer_builtin()
# print(selected is len)
# print(selected(["Rush", "Yes", "Genesis"]))
# ANSWER:


# Exercise 4 — The calling function is not the enclosing function
# Predict the output and explain why the local 1981 is not used.
# year = 1978
# def read_year():
#     return year
# def caller_year():
#     year = 1981
#     return read_year()
# print(caller_year())
# ANSWER:


# Exercise 5 — Shadowing a built-in
# Explain why this function raises TypeError rather than using the built-in sum.
# def total_numbers():
#     sum = 10
#     return sum([1, 2, 3])
# total_numbers()  # Intentional TypeError; keep commented out.
# Rename the local variable so the built-in call succeeds. Predict its result.
# ANSWER:


# Exercise 6 — Write your own enclosing-scope example
# 1. Define a global name message = "Global message".
# 2. Define an outer function that assigns message = "Enclosing message".
# 3. Inside it, define inner() to return message without assigning it locally.
# 4. Have the outer function return inner() and print the outer call's result.
# 5. Add message = "Local message" inside inner before its return, and predict
#    how the result changes.
# 6. Print the global message afterward and explain why it is unchanged.
# Write your code below:


# Optional challenge — Trace all four levels in an album formatter
# Work through this one together when you are ready.
# Define a global constant LABEL_SEPARATOR = " | ".
# Define make_formatter(prefix), with a nested function format_album(album).
# Inside format_album, assign a local title from album["title"].
# Return a string combining prefix, LABEL_SEPARATOR, title, and len(title),
# such as "Favorite | Hemispheres (11 characters)".
# Have make_formatter return format_album itself, without calling it.
# Store make_formatter("Favorite") in formatter, then call formatter with
# an album dictionary containing a "title" key. Print the returned string.
# Explain the scope supplying each of these inside format_album:
# title (local), prefix (enclosing), LABEL_SEPARATOR (global), len (built-in).
# Explain why prefix remains available after make_formatter has returned.
# This retained enclosing binding is a preview of closures.
# Write your code below:
