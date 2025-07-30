import string

def analyse_string(text):
    # Define special characters set
    special_chars = set(string.punctuation)
    
    # Count special characters
    special_count = sum(1 for char in text if char in special_chars)
    
    # Count words
    words_count = len(text.split())
    
    # Count total characters excluding spaces
    total_chars = len(text.replace(" ", "").replace("\n", ""))
    
    return {
        "special character": special_count,
        "words": words_count,
        "total characters": total_chars
    }

# Example usage
text = '''Python has a string format operator %. This functions analogously to
printf format strings in C, e.g. "spam=%s eggs=%d" % ("blah", 2)
evaluates to "spam=blah eggs=2".'''

result = analyse_string(text)
print(result)
