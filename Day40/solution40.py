def translate(sentence):
    vowels = 'aeiou'
    words = sentence.split()
    pig_latin_words = []

    for word in words:
        if word[0].lower() in vowels:
            pig_latin_words.append(word + 'yay')
        else:
            pig_latin_words.append(word[1:] + word[0] + 'ay')

    return ' '.join(pig_latin_words)

# Example usage
a = "i love python"
print(translate(a))  # Output: "iyay ovelay ythonpay"
