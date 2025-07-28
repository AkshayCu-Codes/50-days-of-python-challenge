from textblob import TextBlob

def spelling_checker():
    while True:
        word = input("Enter a word: ").strip()
        blob = TextBlob(word)
        corrected_word = str(blob.correct()).strip()
        if corrected_word.lower() == word.lower():
            print(f"Correct word: {word}")
            return word
        else:
            response = input(f"Did you mean: {corrected_word}? (yes/no): ").strip().lower()
            if response == "yes":
                print(f"Correct word: {corrected_word}")
                return corrected_word
            else:
                print("Let's try again.\n")

if __name__ == "__main__":
    spelling_checker()
