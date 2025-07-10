def index_position(text):
    indexes=[]
    for i in range(len(text)):
        if text[i].islower():
            indexes.append(i)
    return indexes


print(index_position("LovE"))   # Output: [1, 2]
print(index_position("HeLLo"))  # Output: [1, 4]
print(index_position("ABC"))    # Output: []