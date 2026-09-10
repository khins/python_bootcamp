# BOOTCAMP CHECKPOINT 1: SECTIONS 1-8
# Mixed review -- 20 questions, 100 points total
#
# Based on the available lesson files in sections 2-8. No section 1 files
# were present when this quiz was created. No section 9 knowledge is needed.
# Topics: printing, types, arithmetic, variables, functions, strings,
# string methods, Boolean logic, conditionals, and recursion.
#
# HOW TO ANSWER
# - Work in order: question types are intentionally mixed.
# - For coding questions, replace pass with your code.
# - Write multiple-choice letters and written answers in the ANSWER comments.
# - Predict snippet output before running it. Keep snippets commented out;
#   if you want to try them, copy them into the scratch space at the bottom.
# - Functions should return results, except #3, which explicitly prints.
# - Match expected text exactly. Assume inputs meet the stated conditions.
# - No imports, lists, or loops are needed. #19 MUST use recursion.
# - Examples illustrate requirements; grading also considers other valid inputs.
# - No solutions are included so you can attempt the quiz independently.
#
# GRADING GUIDE: EACH QUESTION IS WORTH 5 POINTS
# - Multiple choice: 3 for the choice, 2 for a brief explanation.
# - Coding: 3 for behavior, 1 for boundary cases, 1 for required technique.
# - Other questions have their point breakdown beside the prompt.
# - No deductions for harmless style differences or optional test prints.
# - Unanswered questions remain pending if you request a partial grade.
# When ready, ask: "Grade my sections 1-8 checkpoint review."
#
# Future checkpoint naming: sections_09_16_review.py in section 16,
# sections_17_24_review.py in section 24, sections_25_32_review.py in section 32.
# Section 35 can serve as a final cumulative review when you reach it.


# 1. MULTIPLE CHOICE: TEXT OR MATH? -- 5 points
# Which expression evaluates to the integer 24?
# A. "6" * 4
# B. int("6") * 4
# C. "6" + "4"
# D. str(6 * 4)
# Choose ONE and explain how its result differs from A's result.
# ANSWER:
# B if you don't convert in string 6 then you can't muliply by 4


# 2. PREDICT THE OUTPUT: SEPARATORS -- 5 points
# Write the exact visible output, preserving spaces and line breaks (3 points).
# Explain the roles of sep and end in this snippet (2 points).
#
# print("red", "blue", sep=" / ", end=" -> ")
# print("go", "now", sep="-")
# ANSWER:
# sep in this case is used to put the / character in between red and blue and end will add  -> 
# to the end of the string to print


# 3. CODING: A TWO-CALL STATUS MESSAGE -- 5 points
# Complete show_status using exactly TWO print calls.
# First call: print "load" and "check" as separate arguments, using sep.
# Second call: print "ready". Use end to keep both calls on one line.
# Output must be the following text, followed by a newline:
# load | check -> ready
# Do not return the message or print the entire line in one call.
def show_status():
    print("load", "check", sep="|", end="\n")
    print("ready")

print(show_status())


# 4. EXPLAIN IN WORDS: RETURN VERSUS PRINT -- 5 points
# Consider running this as a .py file, not in an interactive Python prompt:
#
# def welcome_message(name):
#     return f"Welcome, {name}!"
#
# welcome_message("Maya")
#
# A. Does the call display anything? Explain why. (2 points)
# B. Write a call that displays the returned message. (1 point)
# C. Identify the parameter and argument in the snippet. (2 points)
# ANSWER A: It returns Welcome Maya! because the name variable is inside the braces of a f string
# ANSWER B: print(welcome_message("Jay"))
# ANSWER C: the parameter is the variable defined in the function def; an argument is what this variable is set to


# 5. MULTIPLE CHOICE: ARITHMETIC -- 5 points
# What does this display?
# print(23 // 4, 23 % 4, 2 + 3 * 4)
# A. 5.75 3 20
# B. 5 3 20
# C. 5 3 14
# D. 6 1 14
# Choose ONE and explain //, %, and the order of operations here.
# ANSWER: C
# the // is regular divison and % drops the decimal 


# 6. CODING: A DEFAULT PRICE LABEL -- 5 points
# Accept an item name (string) and a nonnegative integer price.
# Give price a default value of 5 in the function definition.
# Return the label shown below. Use an f-string or string concatenation.
# shop_label("Pen") => "Pen costs $5"
# shop_label("Mug", 12) => "Mug costs $12"
# shop_label(price=0, item="Sample") => "Sample costs $0"
def shop_label(item, price=0):
    return f'{item} costs ${int(price)}'

print(shop_label("Pen")) # TypeError: shop_label() missing 1 required positional argument: 'price'
print(shop_label("Mug", 12))
print(shop_label(price=0, item="Sample"))


# 7. TRACE THE VARIABLES -- 5 points
# Predict the three printed values in order (3 points).
# Explain why changing tickets does or does not change saved and total (2 points).
#
# tickets = 4
# saved = tickets
# total = tickets * 7
# tickets = tickets + 2
# print(tickets)
# print(saved)
# print(total)
# ANSWER:
# tickets is 4
# saved is 4
# total is 30


# 8. MULTIPLE CHOICE: TRUTHINESS -- 5 points
# Which value is truthy?
# A. ""
# B. 0
# C. None
# D. " "
# Choose ONE and explain the difference between an empty string and a space.
# ANSWER:
# D ; an empty string evals to False and a space the string have length so it is True


# 9. CODING: THE FIRST HALF -- 5 points
# Accept any string. Return its first half using len(), //, and slicing.
# For odd lengths, exclude the middle character. Handle empty strings too.
# front_half("planet") => "pla"
# front_half("abcde") => "ab"
# front_half("Q") => ""
# front_half("") => ""
def front_half(text):
    mid = len(text) // 2
    return text[0:mid]

print(front_half("planet"))
print(front_half("abcde"))
print(front_half("Q"))
print(front_half(""))


# 10. DEBUG AND EXPLAIN: IMMUTABLE STRINGS -- 5 points
# This code intends to print "hello" but does not do so:
#
word = "HELLO"
word.lower()
print(word)
#
# A. What does it actually print? (1 point)
# B. Why doesn't lower() change word here? (2 points)
# C. Rewrite the snippet correctly in comments. (2 points)
# ANSWER A: HELLO
# ANSWER B: just simply calling the lower() function and not assigning it to anything or doing anything simply has not output
# ANSWER C: in the new version below lower() is called setting the parameter so the so the code has a return now to the print function
#
print(word.lower())


# 11. MULTIPLE CHOICE: SEARCHING -- 5 points
# What does "cocoa".find("z") return?
# A. 0
# B. -1
# C. None
# D. It raises ValueError.
# Choose ONE. Explain how using index("z") instead would differ.
# ANSWER:
# B because the find was False ; if using index it assumes it is in the string so ValueError



# 12. CODING: A CLEAN TOPIC TAG -- 5 points
# Accept any string. Remove surrounding whitespace, convert to lowercase,
# then replace every remaining space with a hyphen. Use string methods.
# Multiple internal spaces should become multiple hyphens.
# topic_tag("  Python Basics  ") => "python-basics"
# topic_tag("GO  NOW") => "go--now"
# topic_tag("  ") => ""
def topic_tag(text):
    return text.lower().strip().replace(" ", "-").replace("  ","-")

print(topic_tag("  Python Basics  "))
print(topic_tag("GO  NOW"))
print(topic_tag("  "))


# 13. PREDICT THE OUTPUT: STRING POSITIONS -- 5 points
# Write each printed result in order (1 point each), then explain why
# text[1:4] contains the characters it does (1 point).
#
text = "notebook"
print(text[0])
print(text[-2])
print(text[1:4])
print(text[::-1])
# ANSWER:
# first character is n
# -2 is o counting from rear of string
# [1:4] is ote because it is char 1 through 4 
# text[::-1] reverses the string 


# 14. CODING: SHIPMENT SIZE -- 5 points
# Accept any integer weight. Return:
# - "Invalid" when weight is below 0 or above 20.
# - "Small" for 0 through 5, inclusive.
# - "Medium" for 6 through 12, inclusive.
# - "Large" for 13 through 20, inclusive.
# Use if / elif / else. Think carefully about every endpoint.
# shipment_size(-1) => "Invalid"
# shipment_size(5) => "Small"
# shipment_size(12) => "Medium"
# shipment_size(20) => "Large"
# shipment_size(21) => "Invalid"
def shipment_size(weight):
    if weight < 0:
        return "Invalid"
    elif weight <= 5:
        return "Small"
    elif weight <=12:
        return "Medium"
    elif weight <= 20:
        return "Large"
    else:
        return "Invalid"


print(shipment_size(-1))
print(shipment_size(5))
print(shipment_size(12))
print(shipment_size(20))
print(shipment_size(21))


# 15. EXPLAIN THE BRANCHES -- 5 points
#
def shipping_offer(total):

    if total < 30:
        return "Standard shipping"
    elif total < 60:
        return "Discount shipping"
    elif total >= 60:
        return "Free shipping"
        

# A. What does shipping_offer(75) return? (1 point)
# B. Explain why the "Free shipping" branch never runs. (2 points)
# C. Describe a correction that gives free shipping for 60 or more,
#    discount shipping for 30 through 59, and standard below 30.
#    Assume total is a nonnegative integer. (2 points)
# ANSWER A: return is Discount shipping
# ANSWER B: the first statement evals to True so other branch can't be reached
# ANSWER C: read the change to shipping_offer function
print(shipping_offer(75))
print(shipping_offer(60))
print(shipping_offer(29))
print(shipping_offer(100))

# 16. MULTIPLE CHOICE: DEFAULTS AND KEYWORDS -- 5 points
# Given this definition:
# def introduction(name, greeting="Hello"):
#     return f"{greeting}, {name}!"
#
# Which call returns "Hi, Sam!"?
# A. introduction("Hi", "Sam")
# B. introduction("Sam")
# C. introduction(greeting="Hi", name="Sam")
# D. introduction(name="Sam", greeting="Hello")
# Choose ONE and explain how the arguments match the parameters.
# ANSWER: C because the parameter greeting is explicity set as well as name
#


# 17. CODING: DOWNLOAD PERMISSION -- 5 points
# Accept three booleans. Return True only when the account is NOT suspended
# AND the person either owns the course OR has a trial.
# Use all three operators: and, or, not. Return a Boolean.
# download_allowed(True, False, False) => True
# download_allowed(False, True, False) => True
# download_allowed(False, False, False) => False
# download_allowed(True, True, True) => False
def download_allowed(owns_course, has_trial, is_suspended):
    if is_suspended == True:
        return False
    elif has_trial == True or owns_course == True:
        return True
    else:
        return False
    

print(download_allowed(True, False, False))
print(download_allowed(False, True, False))
print(download_allowed(False, False, False))
print(download_allowed(True, True, True))


# 18. TRACE A RECURSIVE CALL -- 5 points
#
def step_total(number):
    if number == 0:
        return 0
    return number + step_total(number - 1)
#
# A. Write the sequence of calls starting with step_total(3), including
#    the call that reaches the base case. (2 points)
# B. Write the value returned by each call as the recursion unwinds. (2 points)
# C. What does print(step_total(3)) display? (1 point)
# ANSWER A: number starts at 3 then calls step_total(2) and repeats until number is 0
# ANSWER B: when it unwinds the value is 3 + 2 + 1
# ANSWER C: 6
step_total(0) # returns 0
step_total(1) # returns 1 + that result
step_total(2) # returns 2 + that result
step_total(3) # returns 3 + that result


# 19. CODING: RECURSIVE DOUBLING -- 5 points
# Accept an integer times from 0 through 20.
# Start with 1 and double it times times. Return the resulting integer.
# Your function MUST call itself and move toward a base case.
# Do not use loops, **, or pow(). Multiplication is allowed.
# doubled_from_one(0) => 1
# doubled_from_one(1) => 2
# doubled_from_one(3) => 8
# doubled_from_one(5) => 32
def doubled_from_one(times):
    if times == 0:
        return 1
    return times * doubled_from_one(times -1)

print(doubled_from_one(0))
print(doubled_from_one(1))
print(doubled_from_one(3))
print(doubled_from_one(5))


# 20. WRITTEN REFLECTION: EXPLAIN YOUR RECURSION -- 5 points
# Answer in a short paragraph of about 4-6 sentences, using your #19 solution.
# A. Identify your base case and explain its return value. (2 points)
# B. Explain how each recursive call gets closer to stopping. (1 point)
# C. If the base-case check were removed, what would normally happen in
#    Python, and what is the name of the exception? (1 point)
# D. If return were removed from the recursive-step line but the recursive
#    call still ran, what would doubled_from_one(1) return, and why? (1 point)
# ANSWER:
# the base case is 0 
# each case gets closer to the base case because of subtracting 1
# the error is RecursionError
# 


# SCRATCH SPACE
# Add or uncomment print calls here as you finish each coding question.
# Leave prediction snippets commented until you have written your predictions.
