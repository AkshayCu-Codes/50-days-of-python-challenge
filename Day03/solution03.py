def register_check(register):
    count=0
    for status in register.values():
        if status == 'yes':
            count +=1
    return count

print(register_check({'Anna': 'yes', 'Ben': 'yes', 'Cara': 'no'}))
print(register_check({'Michael': 'yes','John': 'no','Peter': 'yes','Mary': 'yes'}))

# Output

# PS C:\Users\akshay cu\OneDrive\Documents\50-days-of-python-challenge> python Day03/solution03.py"
# 2
# 3


# --------------------------------------------OR-----------------------------------------------------

def register_check(reg):
    return sum(1 for status in reg.values() if status == 'yes')

print(register_check({'Zoe': 'no', 'Luke': 'no'}))  #0
print(register_check({'Jane': 'yes'}))              #1