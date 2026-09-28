# The nonlocal Keyword — Study Summary
# Instructor summary:
# - nonlocal lets a nested function rebind a name in an enclosing function scope.
# - Without that declaration, assignment normally creates a local binding.
# - nonlocal targets an enclosing function binding; global targets the module.
# - The nested function must actually run for its assignment to take effect.
# - An enclosing function's parameters can also be targeted with nonlocal.
# - This supports closures that update retained state between calls.
#
# Clarifications and corrections:
# - Write nonlocal as one word, without a hyphen.
# - Reading an enclosing name does not require nonlocal; rebinding it does.
# - nonlocal requires an existing binding in an enclosing function scope.
#   It cannot create a new global or use a module-level binding as its target.
# - If several enclosing functions bind the same name, the nearest one is used.
# - Put the declaration before using or assigning that name in the same scope.
# - The declaration itself changes no value; an executed assignment does that.
# - Rebinding a name is different from mutating a referenced list or dictionary.
# - Changing an enclosing parameter binding does not reassign the caller's variable.
# - Retained closure bindings can survive the outer call; they are not necessarily
#   discarded as soon as the outer function returns.


# --- 1. A local assignment does not change the enclosing binding ---
def outer_local():
    bubble_tea_flavor = "Black"

    def inner():
        bubble_tea_flavor = "Taro"

    inner()
    return bubble_tea_flavor


print(outer_local())  # Black
# inner assigns its own local name. The outer function's name still refers to Black.


# --- 2. Rebind the enclosing name with nonlocal ---
def outer_nonlocal():
    bubble_tea_flavor = "Black"

    def inner():
        nonlocal bubble_tea_flavor
        bubble_tea_flavor = "Taro"

    inner()
    return bubble_tea_flavor


print(outer_nonlocal())  # Taro
# Both the assignment in inner and the final return in outer_nonlocal use
# the same enclosing binding. No global bubble_tea_flavor is created.


# --- 3. Defining the inner function does not execute its assignment ---
def outer_without_call():
    bubble_tea_flavor = "Black"

    def inner():
        nonlocal bubble_tea_flavor
        bubble_tea_flavor = "Taro"

    return bubble_tea_flavor


print(outer_without_call())  # Black
# There is no inner() call, so the assignment to Taro never runs.


# --- 4. An enclosing parameter can be rebound ---
def choose_name(name=None):
    def fill_missing_name():
        nonlocal name
        if name is None:
            name = "Untitled"

    fill_missing_name()
    return name


print(choose_name())  # Untitled
print(choose_name("Hemispheres"))  # Hemispheres
print(repr(choose_name("")))  # '' — an empty string is not None
original_name = None
print(choose_name(original_name))  # Untitled
print(original_name)  # None
# The nested function rebinds choose_name's parameter, not the caller's variable.
# This self-contained example illustrates the enclosing-parameter pattern
# discussed in the instructor's codebase walkthrough.


# --- 5. Update retained closure state ---
def make_counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment


counter = make_counter()
print(counter())  # 1
print(counter())  # 2
other_counter = make_counter()
print(other_counter())  # 1
print(counter())  # 3
# Each outer call creates its own count binding. The returned increment function
# retains and updates that binding after make_counter has returned.
# += both reads and rebinds count, so nonlocal is needed here.


# --- 6. The nearest enclosing binding is used ---
def outer_levels():
    flavor = "Black"

    def middle():
        flavor = "Green"

        def inner():
            nonlocal flavor
            flavor = "Taro"

        inner()
        return flavor

    middle_result = middle()
    return flavor, middle_result


print(outer_levels())  # ('Black', 'Taro')
# inner updates middle's flavor. It does not skip that binding to reach outer_levels.


# --- 7. Mutating an enclosing list does not rebind its name ---
def collect_artists():
    artists = []

    def add_artist(name):
        artists.append(name)

    add_artist("Rush")
    add_artist("Yes")
    return artists


print(collect_artists())  # ['Rush', 'Yes']
# append() changes the existing list; it does not assign to artists.
# To replace the enclosing binding with artists = [name] inside add_artist,
# a nonlocal artists declaration would be needed.


# --- 8. Recognize missing declarations and missing bindings ---
# Without nonlocal, this update tries to read an unassigned local count:
# def broken_counter():
#     count = 0
#     def increment():
#         count += 1
#         return count
#     return increment()
# broken_counter()  # Intentional UnboundLocalError; keep commented out.
#
# A missing enclosing binding causes SyntaxError, before the function can run:
# def invalid_example():
#     nonlocal nonexistent_enclosing_name
#
# Keep that entire invalid definition commented out. A module-level variable
# with the same name would not satisfy nonlocal's enclosing-function requirement.


# --- 9. Practice: predict, explain, then run ---
# Write predictions in ANSWER comments before uncommenting each exercise.
# Keep intentional-error examples commented out.
# Identify which function scope owns each binding being changed.

# Exercise 1 — Compare assignments
# Predict both outputs and explain the difference between the two functions.
# print(outer_local())
# print(outer_nonlocal())
# ANSWER:


# Exercise 2 — A function must be called
# Predict the output. What line would you add to make it return "After"?
# def outer():
#     message = "Before"
#     def update():
#         nonlocal message
#         message = "After"
#     return message
# print(outer())
# ANSWER:


# Exercise 3 — Rebind a parameter
# Predict all three outputs. Explain why supplied_name remains unchanged.
# supplied_name = None
# print(choose_name(supplied_name))
# print(supplied_name)
# print(choose_name("Tarkus"))
# ANSWER:


# Exercise 4 — Independent counters
# Predict all four outputs. How many separate count bindings are created?
# first = make_counter()
# second = make_counter()
# print(first())
# print(first())
# print(second())
# print(first())
# ANSWER:


# Exercise 5 — Diagnose the scope
# Explain why the inner call raises UnboundLocalError and add the missing
# declaration in the correct place.
# def outer_total():
#     total = 10
#     def increase():
#         total += 5
#     increase()
#     return total
# print(outer_total())  # Keep commented out until the function is corrected.
# ANSWER:


# Exercise 6 — Write your own score tracker
# 1. Define make_score_tracker(start), with a nested add_points(points) function.
# 2. Use nonlocal to increase the enclosing start binding by points.
# 3. Return the updated score from add_points.
# 4. Return add_points itself from make_score_tracker.
# 5. Create a tracker starting at 10, call it with 5 and then 3, and print results.
# 6. Explain why the second call remembers the first update.
# Write your code below:


# Optional challenge — A private album log with a running count
# Work through this one together when you are ready.
# Define make_album_logger(). Inside it, initialize labels = [] and count = 0.
# Define a nested log_album(album) accepting a dictionary with title, artist,
# and year keys. Append a label such as "Hemispheres by Rush (1978)" to labels.
# Increment the enclosing count using nonlocal and return the updated count.
# Define a second nested function get_labels() that returns a shallow copy
# of labels, so appending to that returned list does not change the stored log.
# Return log_album and get_labels as a tuple of function objects.
# Unpack them into log_album, get_labels at the call site, log three albums,
# and print the returned counts and the list supplied by get_labels().
# Create a second logger and verify its initial label list is empty.
# Explain why count needs nonlocal but labels.append(...) does not, and why
# both returned functions from one factory call can access the same labels list.
# Write your code below:
