# BOOTCAMP CUMULATIVE REVIEW: SECTIONS 13-17
# Mixed quiz -- 20 questions, 100 points total
#
# Based on the lesson files in sections 13-17.
# Topics: split/join, zip, nested loops, comprehensions, map/filter/lambda,
# built-in functions, tuples, unpacking, *args, references, copying,
# dictionary access, dictionary methods, and nested dictionaries.
#
# HOW TO ANSWER
# - Work in order; topics and question types are intentionally mixed.
# - Replace pass with your code for coding questions.
# - Put predictions, choices, and explanations in ANSWER comments.
# - Predict what each COMPLETE snippet would do if uncommented, including
#   every assignment and mutation. Do not predict only its starting values.
# - Each prediction snippet starts fresh and is independent of other questions.
# - Snippets and example calls stay commented so the unfinished quiz runs quietly.
# - Copy a whole snippet to the scratch space to experiment after predicting.
# - Functions should return results unless the prompt says otherwise.
# - Assume inputs meet the stated conditions; use the required techniques.
# - No solutions are included. Example results specify required behavior.
# - The copy module is allowed where requested; no other imports are needed.
#
# GRADING: EACH QUESTION IS WORTH 5 POINTS
# - Multiple choice: 3 for the choice, 2 for the explanation.
# - Coding: 3 for behavior, 1 for boundary cases, 1 for required technique.
# - Other question types include their point breakdown in the prompt.
# - Equivalent quote styles are fine. No deductions for harmless style choices.
# - Unanswered questions stay pending when you request a partial grade.
# When ready, ask: "Grade my sections 13-17 review."


# 1. PREDICT: SPLIT AND JOIN -- 5 points
# Write all three outputs (1 each). Explain the difference between split()
# with no argument and split(" ") for this input (2).
#
# text = "  Rush   Yes  "
# words = text.split("")
# print(words) # ["Rush", "Yes"]
# print(" / ".join(words)) # Rush / Yes
# print(text) #"  Rush   Yes  "
# ANSWER:
#   split() with no space splits words and takes out the spaces,
#   split(" ") will split the words and spaces
# split(" ") removes the separator spaces. The empty string "" appears because 
# there is nothing between the two adjacent spaces—it doesn’t contain a space.


# 2. MULTIPLE CHOICE: EQUALITY AND IDENTITY -- 5 points
# What does the final line print?
#   reference section 16\equality_vs_identity.py
original = ["Rush", "Yes"]
alias = original
duplicate = original.copy()
print(original == duplicate, original is duplicate, original is alias)
# A. True True True
# B. True False True
# C. False False True
# D. True False False
# Choose ONE. Explain what == and is compare.
# ANSWER:
#   B 
#   == to compare values or contents ; Use is to check whether two names reference the same object


# 3. CODING: FILTER WITH A COMPREHENSION -- 5 points
# Accept a list of strings and a nonnegative minimum length.
# Return a NEW list of uppercase strings whose ORIGINAL lengths are >= minimum.
# Preserve order and duplicates; leave the input unchanged.
# Use a list comprehension. Do not strip whitespace for this question.
#   section 13\assignment.py
def select_band_names(names, minimum):
    return [name.upper() for name in names if len(name) >= minimum]

print(select_band_names(["Rush", "Yes", "Rush"], 4)) #=> ["RUSH", "RUSH"]
print(select_band_names(["", "a"], 0)) #=> ["", "A"]
print(select_band_names([], 3)) #=> []


# 4. PREDICT: GET, SETDEFAULT, AND NONE -- 5 points
# Write all four outputs (1 each). Explain why the fallback "Guest" does
# not replace the stored None (1).
#   reference section 17\set_default.py
profile = {"nickname": None}
print(profile.get("city", "Unknown")) # Unknown
print("city" in profile) # False 
print(profile.setdefault("nickname", "Guest")) # None
print(profile.setdefault("city", "Chicago")) # Chicago
# ANSWER:
#   since the nickname already had a value and even None is a value then the setdefault wont replace


# 5. PREDICT: STARRED UNPACKING -- 5 points
# Write all four outputs (1 each). Explain why middle has its particular type (1).
#   reference section 15\unpacking_tuples.py
record = ("Kevin", "Chicago", "IL", 60601)
name, *middle, zip_code = record
print(name) # Kevin
print(middle) # ['Chicago', 'IL']
print(zip_code) # 60601
print(type(middle)) # list
# ANSWER:
#   the * spreads the args into a list
# *middle collects the items left over after the first goes to name 
# and the last goes to zip_code.


# 6. CODING: MAP AND FORMAT -- 5 points
# Accept a list of nonnegative numbers and return a list of price strings.
# Use map(), a lambda, list(), and format() with commas and two decimal places.
# Prefix each formatted number with "$". Leave the input unchanged.
#   reference section 14\assignment.py
def price_labels(prices):
    return list(map(lambda number: f'${format(number, ",.2f")}', prices))

print(price_labels([3, 1250.5, 0])) #=> ["$3.00", "$1,250.50", "$0.00"]
print(price_labels([])) #=> []


# 7. TRACE: SHALLOW COPYING -- 5 points
# Write the three outputs (1 each). Explain why appending to an inner list
# affects both structures but replacing an outer-list item does not (2).
#   reference section 16\shallow_and_deep_copies.py
original = [["Rush"], ["Yes"]]
duplicate = original.copy()
duplicate[0].append("Genesis")
duplicate[1] = ["Kansas"]
print(original)                     # [["Rush"], ["Yes"]]
print(duplicate)                    # [["Rush"], ["Yes"]]
print(original[0] is duplicate[0])  # True
# ANSWER:
# Your output is correct. More precisely, .copy() creates a new outer list, but both
#  outer lists still reference the same inner lists. Appending "Genesis" changes a
#  shared inner list, so both see it.
# Both are correct. duplicate[1] = ["Kansas"] replaces an item in duplicate’s outer list, 
# so original[1] stays ["Yes"]. Their first inner list is still shared, so the identity 
# check remains True.

# 8. CODING: CREATE AND MERGE -- 5 points
# Accept a list of [string_key, immutable_value] pairs and a preferences dictionary.
# Create a NEW dictionary with dict(), then use update() so preferences win.
# Return the dictionary. Leave both inputs unchanged. Inputs may be empty;
# pairs may contain repeated keys, with later pairs taking precedence.
#   references section 17\the_dict_function.py, section 17\the_update_method.py

def merge_settings(pairs, preferences):
    final_settings = dict(pairs)
    final_settings.update(preferences)
    return final_settings

print(merge_settings([["volume", 5], ["subtitles", True]], {"volume": 9})) # => {"volume": 9, "subtitles": True}
print(merge_settings([["volume", 2], ["volume", 5]], {})) #=> {"volume": 5}
print(merge_settings([], {})) #=> {}


# 9. PREDICT: ZIP STOPS WHERE? -- 5 points
# Write the two output lines (1 each). Explain which input limits iteration (1)
# and whether either input list changes (2).
#   reference section 13\assignment.py
artists = ["Rush", "Yes", "Genesis"]
counts = [3, 2]
for artist, count in zip(artists, counts):
    print(f"{artist}: {count}")
print(artists)
print(counts)
# ANSWER:
#   Rush: 3
#   Yes: 2
# counts is the shorter list, so zip() stops after two pairs. Neither list changes;
#  "Genesis" remains in artists.

# 10. MULTIPLE CHOICE: TUPLE MUTABILITY -- 5 points
# Each choice starts fresh with record = ("Rush", ["YYZ"]).
# Which line succeeds and leaves record containing ("Rush", ["YYZ", "Limelight"])?
# A. record[0] = "Yes"
# B. record.append("Limelight")
# C. record[1].append("Limelight")
# D. record[1] = ["YYZ", "Limelight"]
# Choose ONE. Explain why changing a contained list differs from replacing
# an item in the tuple.
# ANSWER:
#   C 
# A tuple cannot have its items replaced, but a list stored inside it can still change.
#  Calling append modifies that existing list without replacing the tuple’s item.


# 11. CODING: FILTER, MAP, AND SUM -- 5 points
# Accept a list of integers. Return the sum of the squares of POSITIVE odd numbers.
# Use filter(), map(), and sum(); lambdas or named helper functions are allowed.
# Leave the input unchanged. Do not use loops or comprehensions.
#   reference section 14\assignment.py
def positive_odd_square_total(numbers):
    filtered_numbers = filter(
        lambda number: number % 2 != 0 and number > 0, numbers
    )
    squares = map(lambda number: number ** 2, filtered_numbers)
    return sum(squares)

print(positive_odd_square_total([-3, 0, 1, 2, 5])) # => 26
print(positive_odd_square_total([-1, 2, 4])) # => 0
print(positive_odd_square_total([])) # => 0
print(positive_odd_square_total([2, 3, 7]))


# 12. DEBUG: UPDATE'S RETURN VALUE -- 5 points
# This function should modify target in place and return that SAME dictionary.
# Assume target and changes are separate dictionaries.
#   reference section 17\the_update_method.py
def apply_changes(target, changes):
    target = target.update(changes)
    return target

def apply_changes_fixed(target, changes):
    ''' ANSWER C corrected function'''
    target.update(changes)
    return target
#
settings = {"volume": 5}
result = apply_changes_fixed(settings, {"volume": 9})
# A. What does result hold? (1) # None
# B. What does settings contain afterward, and why? (2)
# C. Write a corrected function in comments using update(). (2)
print(result)
print(settings)
# ANSWER A: {'volume': 9}
# ANSWER B: {'volume': 9} modifies the dictionary that settings and target both refer to.
# ANSWER C: 


# 13. CODING: NESTED LOOPS -- 5 points
# Accept a list of lists of integers. Return a NEW flat list containing only
# positive numbers, preserving their order and duplicates.
# Use two nested for loops and append(); no comprehensions.
# Leave the input and its inner lists unchanged.
#   reference section 13\assignment.py
def collect_positive(groups):
    pos_numb = []
    for group in groups:
        for numb in group:
            if numb > 0:
                pos_numb.append(numb)
    return pos_numb

print(collect_positive([[2, -1], [], [0, 3, 2]])) # => [2, 3, 2]
print(collect_positive([[], [-1, 0]])) # => []
print(collect_positive([])) # => []

# 14. TRACE: REASSIGNMENT VS. CLEAR -- 5 points
# Write all four outputs (1 each). Explain why the alias sees one change
# but does not follow the reassignment (1).
#
playlist = {"YYZ": "Rush"}
shared = playlist
playlist = {}
print(shared)               # {"YYZ": "Rush"}
print(playlist is shared)   # False
result = shared.clear()
print(shared)               # {}
print(result)               # None
# ANSWER:
#   reassignment changes what a name refers to; mutation changes the object itself.

# 15. CODING: VARIABLE ARGUMENTS -- 5 points
# Accept any number of positional integer arguments.
# Return a two-item tuple: (sum_of_even_numbers, count_of_odd_numbers).
# Use *numbers in the function definition and a loop to calculate both values.
# Also write a call in the ANSWER comment that unpacks values = (2, 3, 4)
# into separate positional arguments for your function (required technique).
#   reference section 15\variable_args.py
def summarize_numbers(*numbers):
    even_numbers = 0
    count_of_odd = 0
    for number in numbers:       
        if number % 2 == 0:
            even_numbers += number
        elif number % 2 != 0:
            count_of_odd += 1

    return (even_numbers, count_of_odd)

def summarize_numbers_positional(numbers):
    even_numbers = 0
    count_of_odd = 0
    for number in numbers:       
        if number % 2 == 0:
            even_numbers += number
        elif number % 2 != 0:
            count_of_odd += 1

    return (even_numbers, count_of_odd)

print(summarize_numbers_positional(2, 3, 4, 5)) # => (6, 2)
print(summarize_numbers_positional(-2, -3, 0)) # => (-2, 1)
print(summarize_numbers_positional()) # => (0, 0)
# ANSWER (call using *):
#   Without the star, summarize_numbers(values) would pass one whole tuple as
#  a single argument, so your loop would try to calculate


# 16. PREDICT: ALL, ANY, AND MAX -- 5 points
# Write the four outputs (1 each). Explain why all([]) and any([]) differ (1).
#   reference section 14\assignment.py
print(all([])) # True
print(any([]))  # False 
print(all(map(lambda number: number > 0, [2, 0, 4]))) # False
print(max(["Rush", "Yes", "Asia"], key=len, default="")) # Rush
# ANSWER:
#  for all If the iterable is empty, return True.
#  for any If the iterable is empty, return False.
#   for the lambda all needs to be True for the list but the 0 causes it to be False


# 17. PREDICT: POP AND DEL -- 5 points
# Write all four outputs (1 each). State the error that del menu["cake"]
# would raise if added after this snippet (1).
#   reference section 17\the_pop_method.py
menu = {"tea": 3, "cake": 5}
print(menu.pop("tea", 0))   # 3
print(menu.pop("tea", 0))   # 0
del menu["cake"]            
print(menu)                 # {}
print("tea" in menu)        # False
# ANSWER:
#   KeyError would happen because the cake is gone because the list is empty


# 18. CODING: MAKE NESTED LISTS INDEPENDENT -- 5 points
# Accept a list containing at least one inner list of strings, plus a string title.
# Make a deep copy, append title to its FIRST inner list, and return the copy.
# Use copy.deepcopy() and append(). Add the import above your function.
# Leave the original outer list and ALL its inner lists unchanged.
# The returned first inner list must be a different object from the original.
#   reference section 16\shallow_and_deep_copies.py
import copy
def add_to_copied_group(groups, title):
    new_group = copy.deepcopy(groups)
    new_group[0].append(title)
    return new_group

print(add_to_copied_group([["YYZ"], ["Roundabout"]], "Limelight")) # => [["YYZ", "Limelight"], ["Roundabout"]]
print(add_to_copied_group([[]], "Echoes")) # => [["Echoes"]]

# 19. DEBUG: NESTED DICTIONARY PATHS -- 5 points
# Use this fresh sample for all parts:
#   section 17\nested_dict.py
library = {
    "Rush": {
        "Moving Pictures": {"year": 1981, "songs": ["Tom Sawyer", "YYZ"]},
    },
}
# A. Why does library["Rush"]["year"] raise KeyError? (1)
# B. Write a corrected expression to read the album's year. (1)
# C. Write an expression to read its SECOND song title. (1)
# D. Explain why len(library["Rush"]) and
#    len(library["Rush"]["Moving Pictures"]) differ; give both lengths. (2)
# ANSWER A: year is in in a different nested dict
# ANSWER B:
print(library["Rush"]["Moving Pictures"]["year"])
# ANSWER C:
print(library["Rush"]["Moving Pictures"]["songs"][1])
# ANSWER D:
print(len(library["Rush"])) # 1
print(len(library["Rush"]["Moving Pictures"])) # 2
#   these dictionaries are different in length because the Rush library contains just the 1 album dict
#   whereas the Moving Pictures is the album that is containing 2 songs


# 20. EXPLAIN AND TRACE: DEFINITION STAR VS. CALL STAR -- 5 points
# Write the two printed tuples (1 each). Explain what * does in the function
# definition (1), what it does in the second call (1), and which call passes
# one positional argument rather than two (1).
#   reference section 15\variable_args.py
def capture(*items):
    return items
#
values = ("Rush", "Yes")
print(capture(values))
print(capture(*values))
# ANSWER:
#   Combine *args with other parameters
#   the values passes one positional arg rather than two

# SCRATCH SPACE
# Add calls to completed functions here. Use fresh inputs when testing mutations.
# Write predictions first, then copy entire snippets here to check them.
capture(values)
capture(*values)