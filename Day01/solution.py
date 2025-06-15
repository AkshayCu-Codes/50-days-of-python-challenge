# Solution for Day 1
import math

def divide_or_square(number):
    if number % 5 == 0:
        return round(math.sqrt(number), 2)
    else:
        return number % 5

# Test examples
print(divide_or_square(10))  
print(divide_or_square(7))   

# Output

# PS C:\Users\akshay cu\OneDrive\Documents\50-days-of-python-challenge\Day01> python solution.py
# 3.16
# 2