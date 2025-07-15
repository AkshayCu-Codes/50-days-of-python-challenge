import time

# Data setup
a = range(10000000)
x = set(a)   # Set
y = list(a)  # List
target = 9999999

# Measure time for list lookup
start_list = time.time()
found_in_list = target in y
end_list = time.time()
list_time = end_list - start_list

# Measure time for set lookup
start_set = time.time()
found_in_set = target in x
end_set = time.time()
set_time = end_set - start_set

# Print results
print(f"List lookup time: {list_time:.6f} seconds")
print(f"Set lookup time: {set_time:.6f} seconds")

# Decide which is faster
if set_time < list_time:
    print("✅ Set is faster and should be preferred for lookup tasks.")
else:
    print("✅ List is faster and should be preferred for lookup tasks.")