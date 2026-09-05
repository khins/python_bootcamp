'''
All about type conversions
'''
# 1 Text to integer
age = "25"
print(int(age)+5)

#2 Text to decimal
price = "19.99"
quantity = "3"
print(float(price))
print(int(quantity))

# 3 Number to text print Your score is 95
score = 95
print('Your score is ' + str(score))

#4 Decimal to integer
measurement = 8.9
print(int(measurement))  # out is just 8 simply removes the fractional part

#5 Two-step conversion
value = "42.7"
print(int(float(value)))


