# Scope III: Closures — Study Summary
# Instructor summary:
# - A nested function can access names from its enclosing function's scope.
# - A closure retains access to those enclosing bindings even after the outer
#   function has finished executing.
# - Returning the inner function lets the caller save it and invoke it later.
# - return inner returns a function; return inner() calls it and returns its result.
# - The retained data can be used without making it a global variable.
#
# Clarifications and corrections:
# - The retained data does not disappear and then magically return. Python keeps
#   the enclosing bindings needed by the surviving function available.
# - The outer call has finished, but the captured bindings still exist.
# - A closure retains access to bindings, not a frozen snapshot of their values.
# - Separate calls to the outer function can create separate captured bindings.
# - Not every nested function captures an enclosing variable. It must refer to
#   a name from an enclosing function scope for this closure behavior.
# - Reading a global variable alone is not capturing an enclosing function local.
# - A captured name does not become a global name merely because it survives.
# - Reading an enclosing binding requires no nonlocal declaration. Rebinding it
#   from the inner function would require nonlocal, a separate topic.


# --- 1. Read an enclosing value during the outer call ---
def outer_immediate():
    candy = "Snickers"

    def inner():
        return candy

    return inner() # Calls the function and returns its result


print(outer_immediate())  # Snickers
print(type(outer_immediate()))  # <class 'str'>
# inner reads candy from the enclosing function. Here it is called immediately,
# so the outer function returns a string, not the nested function.
# saved = outer()
# print(saved)

# --- 2. Return the inner function for later use ---
def outer():
    candy = "Snickers"

    def inner():
        return candy

    return inner


the_func = outer()
print(type(the_func))  # <class 'function'>
print(the_func())  # Snickers
print(the_func())  # Snickers
# outer() has finished before either the_func() call begins.
# the_func refers to inner, which retains access to the enclosing candy binding.
# Returning inner does not execute its body.


# --- 3. Captured names remain separate from global names ---
# Leave these intentional errors commented out:
# print(candy)  # NameError: no module-level candy is defined in this lesson
# print(inner())  # NameError: no module-level inner is defined either
#
# We can call the returned function through the_func, but that does not expose
# its enclosing candy name or its original inner name in the global namespace.
# Scope and lifetime are different: a binding can survive without being global.


# --- 4. Create closures with different remembered values ---
def make_candy_reader(candy):
    def read_candy():
        return candy

    return read_candy


read_snickers = make_candy_reader("Snickers")
read_milky_way = make_candy_reader("Milky Way")
print(read_snickers())  # Snickers
print(read_milky_way())  # Milky Way
print(read_snickers())  # Snickers
print(read_snickers is read_milky_way)  # False
# Each outer call creates a function with access to that call's candy binding.
# Calling the second closure does not replace the first closure's binding.


# --- 5. A closure accesses a binding, not an earlier snapshot ---
def make_updated_reader():
    candy = "Snickers"

    def read_candy():
        return candy

    candy = "Twix"
    return read_candy


updated_reader = make_updated_reader()
print(updated_reader())  # Twix
# Defining read_candy did not freeze candy as "Snickers".
# The enclosing binding was reassigned before the returned function was called.


# --- 6. Use a captured setting in later calculations ---
def make_multiplier(factor):
    def multiply(number):
        return number * factor

    return multiply


double = make_multiplier(2)
triple = make_multiplier(3)
print(double(5))  # 10
print(triple(5))  # 15
print(double(8))  # 16
# factor comes from the enclosing call and is retained by the closure.
# number is a local parameter supplied afresh each time multiply is called.
# make_multiplier returns a function; double(5) returns a numeric result.


# --- 7. Captured objects are not automatically copied ---
def make_list_reader(items):
    def read_items():
        return items

    return read_items


artists = ["Rush"]
read_artists = make_list_reader(artists)
artists.append("Yes")
print(read_artists())  # ['Rush', 'Yes']
print(read_artists() is artists)  # True
# The closure's items binding refers to the same list passed into the outer call.
# Mutating that shared list is visible through the closure too.
# Retaining a binding is not the same as making an independent copy of its object.


# --- 8. Practice: predict, explain, then run ---
# Write predictions in ANSWER comments before uncommenting each exercise.
# Distinguish returning a function from calling it and returning its result.
# Keep intentional-error examples commented out.

# Exercise 1 — Function or string?
# Predict all three outputs. Which outer function returns a function object?
print(type(outer_immediate()))
print(type(outer()))
saved = outer()
print(saved())
# ANSWER:
# <class 'str'>
# <class 'function'>
# Snickers

# Exercise 2 — Independent enclosing calls
# Predict all three outputs and explain which value each reader retains access to.
first = make_candy_reader("Reese's Pieces")
second = make_candy_reader("Sour Patch Kids")
print(first())
print(second())
print(first())
# ANSWER:
# Reese's Pieces
# Sour Patch Kids
# Reese's Pieces
# explain which value each reader retains access to: reader retains access to the value that is passed into
first = make_candy_reader("Reese's Pieces")
second = make_candy_reader("Sour Patch Kids")

third = first

print(third())
print(first is third)
print(first is second)

first = make_candy_reader("Reese's Pieces")
third = first

first = make_candy_reader("M&M's")

print(first())
print(third())
print(first is third)

# Exercise 3 — A retained binding
# Predict the output. Why is the earlier value not returned?
def make_reader():
    message = "Before"
    def read():
        return message
    message = "After"
    return read
reader = make_reader()
print(reader())
# ANSWER:
# After
# Why is the earlier value not returned? earlier message is not returned because it is changed later in the function thus Reassignment of the var

# Exercise 4 — Local versus enclosing parameters
# Predict both outputs. Identify where factor and number get their values.
times_four = make_multiplier(4)
print(times_four(3))
print(times_four(10))
# Explain why make_multiplier does not need to remain running. make_multiplier() returns the nested function, not the multiplication result.
# ANSWER:
# 12
# 40

# Exercise 5 — Shared mutable data
# Predict the output. Does make_list_reader copy its input list?
titles = ["Hemispheres"]
reader = make_list_reader(titles)
titles.append("Tarkus")
print(reader())
# ANSWER:
# ['Hemispheres', 'Tarkus']
# does not copy the list


# Exercise 6 — Write your own greeting factory
# Write your code below:
# 1. Define make_greeter(greeting).
def make_greeter(greeting):

    # 2. Inside it, define greet(name) to return a string such as "Hello, Kevin!".
    def greet(name) -> str:
        return f'{greeting}, {name}!'

    return greet

# 3. Have greet use greeting from the enclosing scope and name from its parameter.
# 4. Return greet itself without calling it.
# 5. Create two greeters with different greeting strings and call both with "Kevin".
print(make_greeter("Hello")("Kevin"))
print(make_greeter("Welcome")("Geddy"))
# 6. Predict their output and explain why each retains its own greeting binding.
hello_greeter = make_greeter("Hello")
welcome_greeter = make_greeter("Welcome")

print(hello_greeter("Kevin"))
print(welcome_greeter("Kevin"))
greeter1 = make_greeter("Good morning")
greeter2 = make_greeter("Good evening")

greeter1 = greeter2

print(greeter1("Kevin"))
print(greeter1 is greeter2)

def make_counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment


counter1 = make_counter()
counter2 = make_counter()

print(counter1())
print(counter1())
print(counter2())
print(counter1())

# def make_counter():
#     count = 0

#     def increment():
#         count += 1
#         return count

#     return increment


# counter = make_counter()
# print(counter())

# Optional challenge — Remember an album-label prefix
# Write your code below:
# Work through this one together when you are ready.
# Define make_album_formatter(prefix).
def make_album_formatter(prefix):

    # Inside it, define format_album(album) to return a string such as:
    # "Favorite: Hemispheres by Rush (1978)"
    def format_album(album) -> str:
        return f'{prefix} {album["title"]} by {album["artist"]} ({album["year"]})'

    return format_album

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

print(make_album_formatter("Favorite:")(albums[1]))

# Use prefix from the enclosing scope and the dictionary's title, artist, and year.
# Return format_album itself without calling it.
# Create favorite_formatter with prefix "Favorite" and wishlist_formatter with
# prefix "Wishlist". Call both with the same album dictionary and print the results.
# Then use favorite_formatter in a loop over three album dictionaries and collect
# its returned strings in a NEW list. Print the list after the loop.
# Preserve the input dictionaries and their order.
# Explain which binding is captured, which parameter changes with each inner call,
# and why creating wishlist_formatter does not replace favorite_formatter's prefix.

