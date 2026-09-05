# Review the concepts introduced in the Variables section of the course in this written assessment.

# 1 Create and use variables
product_name = 'Widget 2.0'
price = 100
quantity = 4
total_cost = price * quantity
print(f'The total cost is {total_cost}')

# 2 
points = 10
points = (points + 5) * 2
print(points)

# 3 Predict how assignment works
# prediction :
# prints value 20 then prints 8
first = 8
second = first
first = 20
print(first)
print(second)

# 4 Swap two values
a = "red"
b = "blue"

c = a  # Save "red" before changing a.
a = b  # a now holds "blue".
b = c  # b now holds the saved "red".

print(a)
print(b)

# 5 Update a calculation changing length doesnt update area because area isn't assigned again 
length = 6
width = 4
area = length * width
length = 10
print(area)