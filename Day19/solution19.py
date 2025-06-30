def count_words(sentance):
    return len(sentance.split())


def count_elements(sentance):
    return len(sentance.replace(" ",""))


print(count_words("I love learning"))
print(count_elements("I love learning"))