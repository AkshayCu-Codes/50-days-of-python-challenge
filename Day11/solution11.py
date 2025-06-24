def equal_strings(s1,s2):
    return sorted(s1) == sorted(s2)

print(equal_strings('loveh', 'evol'))     # True
print(equal_strings('abc', 'cab'))       # True
print(equal_strings('abc', 'abcd'))      # False
print(equal_strings('hello', 'olelh'))   # True
print(equal_strings('one', 'neo'))       # True
print(equal_strings('test', 'taste'))    # False

    