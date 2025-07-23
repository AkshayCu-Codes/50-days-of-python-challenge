def words_with_vowels(sentence):
    vowels = set("aeiouAEIOU")
    words = sentence.split()
    return [word for word in words if any(char in vowels for char in word)]

# Example usage
print(words_with_vowels("You have no rhythm"))
# Output: ['You', 'have', 'no']
