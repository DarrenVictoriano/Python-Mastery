"""
These are key methids for numeric types
"""
import math

# the abs function returns the absolute value of a number
print("abs() ---")
print(f'abs(-34.5) : {abs(-34.5)}')
print(f'abs(34.5) : {abs(34.5)}')

# The method ceil() in Python returns ceiling value of x
# i.e., the smallest integer not less than x.
print("\nmath.ceil() ---")
print(f'math.ceil(-23.11) : {math.ceil(-23.11)}')
print(f'math.ceil(300.16) : {math.ceil(300.16)}')
print(f'math.ceil(300.72) : {math.ceil(300.72)}')

# floor() method in Python returns floor of x
# i.e., the largest integer not greater than x.
print("\nmath.floor() ---")
print("math.floor(-23.11) : ", math.floor(-23.11))
print("math.floor(300.16) : ", math.floor(300.16))
print("math.floor(300.72) : ", math.floor(300.72))

# min() function is used to compute the minimum of the values passed in its argument
# and lexicographically smallest value if strings are passed as arguments.
print("\nmin() ---")
print("Minimum of [4,12,43.3,19, 100] is : ", end="")
print(min(4, 12, 43.3, 19, 100))

# This function is used to compute the maximum of the values passed in its argument
# and lexicographically largest value if strings are passed as arguments.
print("\nmax() ---")
print("Maximum of [4,12,43.3,19, 100] is : ", end="")
print(max(4, 12, 43.3, 19, 100))
