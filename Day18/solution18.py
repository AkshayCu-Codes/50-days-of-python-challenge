def any_number(*args):
    if not args:
        return 0.0
    return sum(args)/len(args)

print(any_number(12, 90, 12, 34))     # Output: 37.0
print(any_number(12, 90))             # Output: 51.0
print(any_number(10.5, 3.5, 6))       # Output: 6.666...
print(any_number())                   # Output: 0.0