def only_floats(a,b):
    if isinstance(a,float) and isinstance(b,float):
        return 2
    elif isinstance(a,float) or isinstance(b,float):
        return 1
    else:
        return 0

print(only_floats(12.1, 23))
print(only_floats(10.1, 20.2))
print(only_floats(5, 8))

# Output
# 1
# 2
# 3