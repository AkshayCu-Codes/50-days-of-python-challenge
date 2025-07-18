def check_pangram(s):
    s = s.lower()
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    letters_in_s = set(s)
    result = alphabet.issubset(letters_in_s)
    print(result)
    return result

# Example usage
check_pangram('the quick brown fox jumps over a lazy dog')  # True
check_pangram('hello world')                                # False