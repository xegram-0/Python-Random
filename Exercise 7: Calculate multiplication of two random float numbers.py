# Exercise 7: Calculate multiplication of two random float numbers
# Notes:
#     First random float number must be between 0.1 and 1
#     Second random float number must be between 9.5 and 99.5


import random 
# Assign 2 float variables
num1:float = random.random()
num2:float = random.uniform(9.5,99.5)

print(f"1st float number is {num1}")
print(f"2nd float number is {num2}")

result:float = num1*num2
print(f"The result is {result}")