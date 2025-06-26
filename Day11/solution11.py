def equal_strings(s1,s2):
    return sorted(s1) == sorted(s2)

print(equal_strings('love', 'evol'))    # True
print(equal_strings('abc', 'cab'))       # True
print(equal_strings('abc', 'abcd'))      # False
print(equal_strings('hello', 'olelh'))   # True
print(equal_strings('one', 'neo'))       # True
print(equal_strings('test', 'taste'))    # False

#without sorted function

# def equal_str(s1,s2):
#     if len(s1)!=len(s2):
#         return False
#     count1 = {}
#     count2 = {}

#     for char in s1:
#         count1[char]=count1.get(char,0)+1
#     for char in s2:
#         count2[char]=count2.get(char,0)+1

#     return count1 == count2
    