# BOOTCAMP CUMULATIVE REVIEW: SECTIONS 1-12
# Mixed quiz -- 20 questions, 100 points total
#
# Based on your available files in sections 2-12 and our extend() tutorial.
# No section 1 files were present. This is an extra cumulative checkpoint.
# Topics: types, arithmetic, variables, functions, strings, control flow,
# recursion, list indexing, iteration, debugging, and list mutations.
#
# HOW TO ANSWER
# - Work in order; topics and question types are intentionally mixed.
# - Replace pass with your code for coding questions.
# - Put predictions, multiple-choice letters, and explanations in ANSWER comments.
# - Predict before running. Snippets stay commented so they cannot interfere
#   with your solutions. Copy snippets to the scratch space to experiment.
# - Functions should return results unless the prompt explicitly says to print.
# - Assume inputs meet the stated conditions. No imports are needed.
# - Use basic loops and methods you have practiced; no comprehensions needed.
# - No solutions are included. Example results describe required behavior.
#
# GRADING: EACH QUESTION IS WORTH 5 POINTS
# - Multiple choice: 3 for the choice, 2 for the explanation.
# - Coding: 3 for behavior, 1 for boundary cases, 1 for required technique.
# - Other question types show their breakdown beside the prompt.
# - Equivalent quote styles in list output are fine.
# - No deductions for harmless style choices or optional test prints.
# - Unanswered questions stay pending when you request a partial grade.
# When ready, ask: "Grade my sections 1-12 review."


# 1. MULTIPLE CHOICE: NUMBERS AND TEXT -- 5 points
# What does this print?
print(int("17") // 5, 17 % 5, "3" * 2)
# A. 3 2 33
# B. 3 2 6
# C. 3.4 2 33
# D. 3 3 33
# Choose ONE. Explain what // and % calculate and why the last value appears.
# ANSWER:
#  A, the // is a divisor that returns the whole part so 3 and 17 mod 5 is 2 then the final is the string 3 twice


# 2. PREDICT THE OUTPUT: EXTEND AND ITS RETURN -- 5 points
# Write the three printed results in order (1 point each).
# Explain the difference between changing a list and returning a value (2 points).
#
songs = ["Limelight"]
# result = songs.extend(["Freewill", "YYZ"])
# print(songs)
# print(result)
# print(len(songs))
# ANSWER:
# songs is the list "Limelight"
# result is going to be None because the return value to extend is None
# the len of songs is 1


# 3. CODING: CLEAN LABEL WITH A DEFAULT -- 5 points
# Accept a name string and a nonnegative integer count, defaulting to 1.
# Strip surrounding whitespace from name and convert it to lowercase.
# Return the exact label format below using an f-string.

# Keep the word "tracks" even when count is 1.
def practice_label(name, count=1):
    return f'{name.strip().lower()}: {count} tracks'

print(practice_label("  RUSH  ")) #=> "rush: 1 tracks"
print(practice_label(" Yes ", 3)) #=> "yes: 3 tracks"
print(practice_label(count=0, name=" Demo ")) #=> "demo: 0 tracks"


# 4. DEBUG AND EXPLAIN: USE THE ARGUMENT -- 5 points
# This function should return the first matching index, or -1 if absent.
# Instead, it searches the wrong list.
#
favorites = ["Rush", "Yes"]
def find_band(bands, target):
    for index, band in enumerate(favorites):
        if band == target:
            return index
    return -1
#
# A. What does find_band(["Genesis", "Rush"], "Rush") actually return? (1)
# B. Identify the bug and explain why testing only with favorites hides it. (2)
# C. Write the corrected function in comments. Use enumerate(), not index(). (2)
# ANSWER A: the function call returns 0 
# ANSWER B: the bug is that it is searching the wrong list
# ANSWER C: it now returns 1
def find_band_fix(bands, target):
    for index, band in enumerate(bands):
        if band == target:
            return index
    return -1


print(find_band_fix(["Genesis", "Rush"], "Rush"))


# 5. MULTIPLE CHOICE: APPEND OR EXTEND? -- 5 points
# Each choice starts with a fresh list: words = ["go"]
# Which line makes words equal to ["go", "cat", "dog"]?
# A. words.append(["cat", "dog"])
# B. words.extend("catdog")
# C. words.extend(["cat", "dog"])
# D. words = words.extend(["cat", "dog"])
# Choose ONE. Explain what happens in TWO of the other choices.
# ANSWER:
#   Choice is C; in choice D for instance the return value of extend is None and choice B it isn't extending the list just a string

print("-" * 45)
# 6. CODING: FILTER AND CLEAN -- 5 points
# Accept a list of strings and a nonnegative integer minimum.
# Build and return a NEW list. For each string, strip its surrounding whitespace,
# then keep its lowercase version only if the cleaned length is >= minimum.
# Preserve order and leave the input list unchanged. Use a loop and append().
# clean_long_names([" RUSH ", "Yes", "  GENESIS "], 4) => ["rush", "genesis"]
# clean_long_names(["  ", " A "], 1) => ["a"]
# clean_long_names(["  "], 0) => [""]
# clean_long_names([], 3) => []
def clean_long_names(names, minimum):
    new_list = []
    for w in names:
        temp = w.strip().lower()
        if len(temp) >= minimum:
            new_list.append(temp)

    return new_list 


print(clean_long_names([" RUSH ", "Yes", "  GENESIS "], 4))
print(clean_long_names(["  ", " A "], 1))
print(clean_long_names(["  "], 0))
print(clean_long_names([], 3))

# 7. PREDICT THE OUTPUT: SLICE REPLACEMENT -- 5 points
# Write the three outputs (1 point each). Explain why the length changes,
# including which positions the slice replaces (2 points).
#
supplies = ["socks", "lamp", "tent", "blanket", "water"]
# supplies[1:4] = ["food", "map"]
# supplies[-1] = "tea"
# print(supplies)
# print(len(supplies))
# print(supplies[:2])
# ANSWER:
# The first output is the supplies which is the list ["socks", "lamp", "tent", "blanket", "water"]
# The second print is the length of the list which is 5
# the third print will print ['socks', 'lamp']


# 8. CODING: RANGE AND DIVISIBILITY -- 5 points
# Accept integers start and stop with start <= stop, including negatives.
# Return the sum of the EVEN numbers from start through stop, inclusive.
# Use range(), a loop, and %. Do not use sum().

def even_range_total(start, stop):
    total = 0 
    for i in range(start, stop + 1):
        if i % 2 == 0:
            total += i

    return total

print(even_range_total(1, 6)) # => 12
print(even_range_total(-3, 2)) # => 0
print(even_range_total(4, 4)) # => 4
print(even_range_total(3, 3)) # => 0


# 9. EXPLAIN: PRINT, RETURN, AND STRING IMMUTABILITY -- 5 points
# Consider running this in a .py file:
#
def quiet_label(text):
    text.lower()
    return text

quiet_label("RUSH")
print(quiet_label("YES"))
#
# A. What visible output does the entire snippet produce? (2)
# B. Why doesn't lower() change text here? (1)
# C. Rewrite the function in comments so it RETURNS lowercase text,
#    and show a call that displays its returned value. (2)
# ANSWER A: prints YES
# ANSWER B: it simply calls the string method but the return output of lower() does not go anywhere
# ANSWER C: This rewrite now returns the lower case version
def quiet_label_fix(text):
    
    return text.lower()

print(quiet_label_fix("YES"))



# 10. PREDICT THE OUTPUT: REVERSE ITERATION -- 5 points
# Write the exact output lines (3 points).
# Explain why the original list keeps its order and why numbering starts at 1 (2).
#
names = ["Homer", "Bart", "Lisa"]
for position, name in enumerate(reversed(names), start=1):
    if len(name) == 4:
        print(f"{position}: {name[::-1]}")
print(names)
# ANSWER:
# it will print 1: asiL 2: traB


# 11. CODING: BOOLEAN PERMISSION -- 5 points
# Accept three booleans. Return True only when the user is NOT blocked
# AND either owns the album OR has a trial. Otherwise return False.
# Use and, or, and not in your solution. Return a Boolean, not a string.

def can_play(owns_album, has_trial, is_blocked):
    return not is_blocked and (owns_album or has_trial)


print(can_play(True, False, False)) #=> True
print(can_play(False, True, False)) #=> True
print(can_play(False, False, False)) #=> False
print(can_play(True, True, True)) #=> False

# 12. DEBUG AND EXPLAIN: WHICH LIST SHOULD POP? -- 5 points
# Intended behavior: build a new list by reading numbers in order.
# Values > 5 are added to the new list. Each value <= 5 removes the
# last item from the NEW list. The input list must remain unchanged.
# Assume valid inputs never require popping from an empty new list.
#
def build_queue(numbers):
    
    queue = []
    for number in numbers:
        
        if number <= 5:            
            queue.pop()
        else:
           queue.append(number)                            
               
    return queue
#
print(build_queue([10, 20, 2, 30]))

# A. Which line is wrong, and what should it be? (2)
# B. Why is removing items from the input while iterating over it risky? (1)
# C. With the correction, trace queue after EACH item of [10, 20, 2, 30]. (2)
# ANSWER A: the pop was in the wrong position
# ANSWER B: its risky because you are modifying the input that you are looping over
# ANSWER C: it first adds 10 then adds 20 hits 2 sees that its less and pops queue which removes 20 and finally adds 30


# 13. MULTIPLE CHOICE: NESTED INDEXING -- 5 points
bands = [["Rush", "Yes"], ["Genesis", "Kansas"]]
# What does bands[1][0][-1] evaluate to?
# A. "Kansas"
# B. "s"
# C. "G"
# D. "Genesis"
# Choose ONE and explain the three indexing steps.
# ANSWER: B



# 14. CODING: EXTEND INSIDE A FUNCTION -- 5 points
# Accept two separate lists of strings, current and additions.
# Extend current in place with every item from additions, then RETURN current.
# Use extend(). Do not modify additions. Both lists may be empty.
#

# After the call, tracks and updated should both contain:
# ["YYZ", "Freewill", "Limelight"]
# extra should still contain ["Freewill", "Limelight"].
# add_tracks([], []) => []
def add_tracks(current, additions):
    current.extend(additions)
    return current

tracks = ["YYZ"]
extra = ["Freewill", "Limelight"]
updated = add_tracks(tracks, extra)
print(updated)

# 15. TRACE THE VARIABLES: TWO NAMES, ONE LIST -- 5 points
# Write the three printed values (1 point each).
# Explain why this behaves differently from assigning an integer to another
# variable and then assigning a new integer to the first variable (2 points).
#
# original = ["red", "blue"]
# other = original
# other.append("green")
# print(original)
# other = other.extend(["gold"])
# print(other)
# print(original)
# ANSWER:


# 16. CODING: RECURSION CHECK -- 5 points
# Accept an integer number from 0 through 20.
# Return number + (number - 1) + ... + 1, or 0 when number is 0.
# Your function MUST call itself. Do not use loops or sum().

def countdown_total(number):
    if number == 0:
        return 0

    return number + countdown_total(number - 1)


print(countdown_total(0)) #=> 0
print(countdown_total(1)) #=> 1
print(countdown_total(4)) #=> 10
print(countdown_total(6)) #=> 21

# 17. PREDICT THE OUTPUT: REMOVE, POP, AND DEL -- 5 points
# Write the three outputs (1 point each).
# Explain how remove("a") chooses its item and how pop() chooses its item (2).
#
# letters = ["a", "b", "a", "c", "d"]
# removed = letters.remove("a")
# last = letters.pop()
# del letters[1:2]
# print(letters)
# print(removed)
# print(last)
# ANSWER:
# the first print is the letters list ["a", "b", "a", "c", "d"]
# the second print removed is ["b", "a", "c", "d"]
# the third print is ["a", "b", "a", "c"]


# 18. DEBUG AND EXPLAIN: EARLY RETURN -- 5 points
# This should return True if every number is even, and False otherwise.
# An empty list should return True for this exercise.
#
def every_even(numbers):
    for number in numbers:
        if number % 2 != 0:
            return False
        return True
#
# A. What does every_even([2, 3]) actually return, and why? (2)
# B. What does every_even([]) actually return? (1)
# C. Write the corrected function in comments. Keep the loop. (2)
# ANSWER A: before modifiction the function returns True because once through the loop it simply returns True
print(every_even([2, 3]))
# ANSWER B: as is the function will return None for an empty list
print(every_even([]))
# ANSWER C:
def every_even_fix(numbers):

    for number in numbers:
        if number % 2 != 0:
            return False
    return True

print(every_even_fix([2, 3]))
print(every_even_fix([2, 4]))

# 19. CODING: FIRST MATCHING POSITION -- 5 points
# Accept two lists of equal length (possibly empty).
# Return the FIRST index where their elements are equal, or -1 if none match.
# Use enumerate() and indexing. Do not use index(). Leave both lists unchanged.

def first_shared_position(first, second):
    for index, value in enumerate(first):
        if value == second[index]:
            return index

    return -1

print(first_shared_position([1, 2, 3], [9, 2, 3])) #=> 1
print(first_shared_position(["a"], ["a"])) #=> 0
print(first_shared_position([1, 2], [2, 1])) #=> -1
print(first_shared_position([], [])) #=> -1


# 20. PREDICT AND EXPLAIN: SORT, REVERSE, CLEAR -- 5 points
# Write the four printed results (1 point each).
# Explain why a method's effect on a list and its return value must be
# considered separately (1 point).
#
# numbers = [8, 2, 5]
# result = numbers.sort()
# print(numbers)
# print(result)
# numbers.reverse()
# print(numbers)
# numbers.clear()
# print(numbers)
# ANSWER:
# first print is numbers list [8, 2, 5]
# second print is [2, 5, 8]
# third print is [8, 5, 2]
# finals print is []


# SCRATCH SPACE
# Add calls to completed functions here. Use fresh lists when checking mutations.
# Keep prediction snippets commented until you have written your answers.

# Your score: 76/100. Your coding questions earned 35/35,
#  including your corrected #19! Most lost points came from 
# predicting list changes and leaving explanations incomplete.
