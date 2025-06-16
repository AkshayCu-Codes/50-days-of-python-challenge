def convert_add(lst):
    return sum([int(i) for i in lst])

# Test examples
print(convert_add(['10', '20', '30']))
print(convert_add(['0', '0', '0']))  
print(convert_add(['-5', '5']))        


# Output

# PS C:\Users\akshay cu\OneDrive\Documents\50-days-of-python-challenge> python Day02/solution.py"
# 60
# 0
# 0