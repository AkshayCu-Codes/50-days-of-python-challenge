def longest_word(words):
    length_word=[]
    for word in words:
        length_word.append([len(word),word])
    return max(length_word)

print(longest_word(['Java','Javascript','Python']))