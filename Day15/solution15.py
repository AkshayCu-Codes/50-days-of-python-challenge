def same_in_reverse(text):
    return text==text[::-1]

print(same_in_reverse("dad"))       # Output: True
print(same_in_reverse("python"))    # Output: False
print(same_in_reverse("level"))     # Output: True
