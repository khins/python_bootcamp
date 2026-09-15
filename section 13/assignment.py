pizzas = ['mushroom', 'pepporin', 'meat lovers', 'hawaiin']

print(pizzas.index("meat lovers"))

if "mushroom" in pizzas:
    print(pizzas.index("mushroom"))



# Define an encrypt_message function that accepts a string.
# The input string will consist of only alphabetic characters.
# The function should return a string where all characters have been moved
# "up" two spots in the alphabet. For example, "a" will become "c".
def encrypt_message(string):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    encrypted = ""

    for letter in string:
        enc_letter_index_pos = (alphabet.index(letter) + 2) % 26
        encrypted += alphabet[enc_letter_index_pos]

    return encrypted



# EXAMPLES
print(encrypt_message("abc"))  # => "cde"
print(encrypt_message("xyz"))  # => "zab"
print(encrypt_message(""))     # => ""


# copy method
molly_hatchet =[
    "Flirtin' with Disaster",
    "Dreams I'll Never See",
    "Whiskey Man",
    "Gator Country",
    "Bounty Hunter",
    "Fall of the Peacemakers",
    "Beatin' the Odds",
    "Boogie No More",
    "Bloody Reunion",
    "Satisfied Man",
    "The Rambler",
    "It's All Over Now",
]

more_molly = molly_hatchet.copy()
molly_hatchet.remove("Flirtin' with Disaster")
even_more_molly = more_molly[:]
print(molly_hatchet)
print(more_molly)
print(even_more_molly)

yes_men = [
    "Jon",
    "Chris",
    "Steve",
    "Rick",
    "Alan",
    "Bill",
    "Trevor",
    "Geoff",
    "Billy",
    "Jon",
    "Jay",
    "Peter",
    "Tony",
    "Patrick",
    "Trevor",
    "Igor",
    "Benoît",
]

print(", ".join(yes_men))
# split() turns a string into a list; join() combines strings from a list into one string.

# Define a word_lengths function that accepts a string.
# It should return a list with the lengths of each word.
def word_lengths(string):
    new_list = []
    split_string = string.split(" ")
    for word in split_string:
        new_list.append(len(word))

    return new_list


# EXAMPLES
print(word_lengths("Mary Poppins was a nanny"))     # => [4, 7, 3, 1, 5]
print(word_lengths("Somebody stole my donut"))      # => [8, 5, 2, 5]


# Define a cleanup function that accepts a list of strings.
# The function should return the strings joined together by a space.
# There's one BIG problem -- some of the strings are empty or only consist of spaces!
# These should NOT be included in the final string
def cleanup(list):
    cleaned_string = []
    for word in list:
        if word.isspace() or len(word) == 0:
            continue

        cleaned_string.append(word)

    return " ".join(cleaned_string)


print(cleanup(["cat", "er", "pillar"]))             # => "cat er pillar"
print(cleanup(["cat", " ", "er", "", "pillar"]))    # => "cat er pillar"
print(cleanup(["", "", " ", ""]))                   # => ""

# zip function
for ym, pz in zip(yes_men, pizzas):
    print(f'{ym} {pz}')

american_sodas = [
    "Coca-Cola",
    "Pepsi",
    "Mountain Dew",
    "Dr Pepper",
    "Sprite",
    "7Up",
    "Fanta",
    "A&W Root Beer",
    "Sunkist",
    "Sierra Mist",
    "Canada Dry",
    "Barq's",
    "RC Cola",
    "Mello Yello",
    "Big Red",
]

all_favs = []

for fav in american_sodas:
    for f in fav:
        all_favs.append(f)

# print(all_favs)

# Define a nested_sum function that accepts a list of lists of numbers
# It should return the sum of the values
# The list may contain empty lists
def nested_sum(lists):
    list_sum = 0
    for number in lists:
        for n in number:
            list_sum += n

    return list_sum


# EXAMPLES
print(nested_sum([[1, 2, 3], [4, 5]]))            # => 15
print(nested_sum([[1, 2, 3], [], [], [4], [5]]))  # => 15
print(nested_sum([[]]))                           # => 0


# Define a fancy_concatenate function that accepts a list of lists of strings
# The function should return a concatenated string
# The strings in a list should only be concatenated if the length of the list is 3

def fancy_concatenate(list):
    new_string = ""
    for letter in list:
        if len(letter) == 3:
            for i in letter:
                new_string += i

    return new_string

# EXAMPLES
print(fancy_concatenate([["A", "B", "C"]]))                         # => "ABC"
print(fancy_concatenate([["A", "B", "C"], ["D", "E", "F"]]))        # => "ABCDEF"
print(fancy_concatenate([["A", "B", "C"], ["D", "E", "F", "G"]]))   # => "ABC"
print(fancy_concatenate([["A", "B", "C"], ["D", "E"]]))             # => "ABC"
print(fancy_concatenate([["A", "B"], ["C", "D"]]))                  # => ""

# list comprehensions
numbers = [3, 4, 5, 6, 7]
squares = [number ** 2 for number in numbers]
print(squares)

print([ym.upper() for ym in yes_men])

# comprehensions and filtering results
print(["abcdefghihjklmnopqrstuvwxyz".index(char) for char in "donut"])    

popular_donuts = [
    "Glazed",
    "Chocolate Frosted",
    "Boston Cream",
    "Jelly",
    "Apple Fritter",
    "Powdered Sugar",
    "Old Fashioned",
    "Cinnamon Sugar",
    "Maple Bacon",
    "Crumb",
    "Blueberry",
    "Strawberry Frosted with Sprinkles",
]

creamy = [donut for donut in popular_donuts if "Cream" in donut]
print(creamy)

# Uncomment the commented lines of code below and complete the list comprehension logic

# The floats variable should store the floating point values
# for each string in the values list.
values = ["3.14", "9.99", "567.324", "5.678"]
floats = [float(numb) for numb in values]
print(floats)


# The letters variable should store a list of 5 strings.
# Each of the strings should be a character from name concatenated together 3 times.
# i.e. ['BBB', 'ooo', 'rrr', 'iii', 'sss']
name = "Boris"
letters = [val * 3 for val in name]
print(letters)

# The 'lengths' list should store a list with the lengths
# of each string in the 'elements' list
elements = ["Hydrogen", "Helium", "Lithium", "Boron", "Carbon"]
lengths = [len(element) for element in elements]
print(lengths)


# Declare a destroy_elements function that accepts two lists.
# It should return a list of all elements from the first list
# that are NOT contained in the second list.
# Use list comprehension in your solution.
#
def destroy_elements(list1, list2):
    new_list = []
    # for element in list1:        solved with loop
    #     if not element in list2:
    #         new_list.append(element)
    return [element for element in list1 if element not in list2]


print(destroy_elements([1, 2, 3], [1, 2]))     # => [3]
print(destroy_elements([1, 2, 3], [1, 2, 3]))  # => []
print(destroy_elements([1, 2, 3], [4, 5]))     # => [1, 2, 3]