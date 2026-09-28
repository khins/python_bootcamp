# The global Keyword — Study Summary
# Instructor summary:
# - Assignment inside a function normally creates or updates a local binding.
# - global x tells Python to resolve x in that function through the module's
#   global namespace rather than treating it as a local name.
# - With that declaration, x = 15 inside the function rebinds the module's x.
# - A function can also create a previously absent global name by assigning to it.
# - Global changes can make behavior depend on the order of function calls.
# - Prefer explicit parameters and returned results when they express the task
#   clearly; understand global for cases where shared module state is intended.
#
# Clarifications and corrections:
# - global is a declaration, not an assignment. It does not create a value alone.
# - A new global binding appears when the assignment executes, not merely when
#   the function is defined or when its global declaration is encountered.
# - Reading an existing global requires no global statement.
# - Place the declaration before using or assigning that name in the function.
# - A global name belongs to the module where the function is defined, not
#   automatically to every file in a project or to the calling function.
# - Rebinding a name differs from mutating an object it refers to. Calling
#   append() on a global list does not itself rebind the list's name.
# - global does not target a surrounding function's local variable; nonlocal
#   handles that separate case.


# --- 1. A local assignment leaves the global unchanged ---
x = 10


def change_local():
    x = 15
    return x


print(x)  # 10
print(change_local())  # 15
print(x)  # 10
# The function's x and the module's x are different bindings.
# Returning the local value does not automatically assign it to the global name.


# --- 2. Declare the name global before assigning ---
def change_stuff():
    global x
    x = 15


print(x)  # 10
change_stuff()
print(x)  # 15
# The assignment changes the module-level x. There is no separate local x here.
# change_stuff() returns None because it has no return statement.
# Its effect on x is separate from its return value.


# --- 3. Read a global without a declaration ---
def read_x():
    return x


print(read_x())  # 15
# This function only reads x, so normal name lookup reaches the module binding.
# A global statement would be unnecessary for this read.


# --- 4. Create a global through an executed assignment ---
def create_status():
    global status
    status = "Ready"


# print(status)  # Intentional NameError before the first call; keep commented out.
create_status()
print(status)  # Ready
# Defining create_status did not create status. Running its assignment did.


def declare_only():
    global declared_only_example


declare_only()
# print(declared_only_example)  # Intentional NameError; no value was assigned.


# --- 5. Update an existing global counter ---
play_count = 0


def record_play():
    global play_count
    play_count += 1
    return play_count


print(record_play())  # 1
print(record_play())  # 2
print(play_count)  # 2
# += both reads and assigns the name, so global is needed for this rebinding.


def broken_record_play():
    play_count += 1


# broken_record_play()  # Intentional UnboundLocalError; keep commented out.
# Without global, play_count is local to that function, but += tries to read
# its value before any local value has been assigned.


# --- 6. Distinguish object mutation from name reassignment ---
artists = ["Rush"]


def add_artist(name):
    artists.append(name)


def replace_artists():
    global artists
    artists = ["Genesis"]


add_artist("Yes")
print(artists)  # ['Rush', 'Yes']
# append() mutates the existing list. add_artist does not assign to artists.
replace_artists()
print(artists)  # ['Genesis']
# This assignment points the global name to a different list object.
# Without global, that assignment would create a local artists binding instead.


# --- 7. Return a result instead of changing shared state ---
def next_play_count(current_count):
    return current_count + 1


count = 0
count = next_play_count(count)
print(count)  # 1
# Here the function receives its input explicitly, and the caller stores the
# returned value. The function does not need to know a global variable's name.


# --- 8. Practice: predict, explain, then run ---
# Write predictions in ANSWER comments before uncommenting each exercise.
# Keep intentional-error calls commented out.
# Use each exercise's starting values to trace its changes in order.

# Exercise 1 — Local assignment
# Predict both outputs. Which score does reset_score assign?
# score = 10
# def reset_score():
#     score = 0
# print(score)
# reset_score()
# print(score)
# ANSWER:


# Exercise 2 — Global assignment
# Predict both outputs. Explain what the declaration changes.
# score = 10
# def reset_global_score():
#     global score
#     score = 0
# print(score)
# reset_global_score()
# print(score)
# ANSWER:


# Exercise 3 — Creation depends on execution
# In a fresh script, explain which line first creates the global message binding.
# def prepare_message():
#     global message
#     message = "Ready"
# prepare_message()
# print(message)
# What happens if the call to prepare_message() is removed?
# ANSWER:


# Exercise 4 — Read or rebind?
# Explain why the first function works but calling the second raises
# UnboundLocalError. Correct the second function to update the global total.
# total = 5
# def get_total():
#     return total
# def increase_total():
#     total += 1
# print(get_total())
# increase_total()  # Intentional error; keep commented out until corrected.
# ANSWER:


# Exercise 5 — Mutate a list
# Predict the final output. Why does add_title not require global titles?
# titles = ["Hemispheres"]
# def add_title():
#     titles.append("Tarkus")
# add_title()
# print(titles)
# How would assigning titles = ["Tarkus"] inside the function differ?
# ANSWER:


# Exercise 6 — Write your own counter
# 1. Define a module-level variable songs_played = 0.
# 2. Define log_song() to increment it using global and return its new value.
# 3. Call log_song() twice and print each returned value.
# 4. Print songs_played afterward and predict all three outputs.
# 5. Explain why the result of a call depends on earlier calls.
# 6. Write an alternative increment_count(count) that returns count + 1
#    without accessing songs_played. Show the caller saving its result.
# Write your code below:


# Optional challenge — Track added albums
# Work through this one together when you are ready.
# Define two module-level names: album_log = [] and albums_added = 0.
# Define log_album(title) to append the title to album_log, increment
# albums_added, and return the new count.
# Use global for the name you reassign. Explain why appending to album_log
# does not require a global declaration for that name.
# Define reset_album_log() to clear the existing list with clear() and set
# albums_added back to 0. Use the appropriate global declaration there too.
# Log three titles and print the list and count outside the functions.
# Reset the log and print both again; expect [] and 0.
# Finally explain how passing a list and returning a count could make the
# functions' dependencies more explicit than relying on module state.
# Write your code below:
