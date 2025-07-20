def count_the_vowels(s):
    vowels = 'aeiouAEIOU'
    unique_vowels = set()
    for char in s:
        if char in vowels:
            unique_vowels.add(char.lower())
    return len(unique_vowels)

print(count_the_vowels("Hello World!"))  # Output: 3