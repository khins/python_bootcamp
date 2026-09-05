'''
Questions for this assignment
What is a function?
   Is a reusable block of code

Tell me a little about parameters, arguments, and return values.
    parameters are names in the function definition
    arguments are what a defined function takes in for input to so the code block can perform task
    return values are the output that the function sends out to the calling block of code

What is a default argument? How do you define one?
    a default argument is a value that is set in case the calling code doesn't send
    example: def some_func(myval=100)

What data type represents nothingness or nonexistence or emptiness?
    None

What is the difference between positional arguments and keyword arguments?
    Positional arguments match parameters by order. Keyword arguments match by name 
    in the function call, rather than the definition. In ordinary calls, 
    positional arguments come before keyword arguments.
'''
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Kevin", greeting="Hi"))