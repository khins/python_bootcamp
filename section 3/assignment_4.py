'''
Double check your understanding of numbers, mathematical operations, expressions, Booleans and more in this quick written assignment!
'''
# 1 Basic arithmetic Print their sum, difference, product, and division result.
a = 17
b = 5
print(a + b)
print(a - b)
print(a * b)
print(a / b)

#2 Division operators 
print(17 / 5) # this version of division retains decimal
print( 17 // 5) # this division drops the decimal
print(f'mod operation  {17 % 5}') # rounds down, and % as returning the remainder (2 here)

#3 Order of operations  predict
'''
4 + 3 * 2    = 10
(4 + 3) * 2  = 14
2 ** 3 + 1   = 9
'''
print(4 + 3 * 2 )
print((4 + 3) * 2)
print(2 ** 3 + 1 )

# 4 Comparisons and Booleans 
x = 10
y = 12
print(x > y)
print(x == y)
print(x != y)


# 5 Combine conditions
temperature = 22
print(temperature >= 18 and temperature <= 25)
temperature = 25
print(temperature >= 18 and temperature <= 25)
temperature = 30
print(temperature >= 18 and temperature < 25)