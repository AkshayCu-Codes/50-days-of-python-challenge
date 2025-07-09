def all_the_same(items):
    if not items:
        return True  # empty input is considered "all the same"
    first = items[0]
    return all(element == first for element in items)

# Example usage
print(all_the_same(["Mary", "Mary", "Mary"]))  # Output: True
print(all_the_same([1, 2, 1]))                 # Output: False
print(all_the_same("aaa"))                     # Output: True
print(all_the_same(""))                        # Output: True (empty string)
