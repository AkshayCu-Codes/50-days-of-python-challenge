def sort_words(sentance):
    s=sentance.replace(" ","").lower()

    unique_letters = sorted(set(s))

    return unique_letters


print(sort_words("Hi Hello"))