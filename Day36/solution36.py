def count(s):
    freq={}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq

print(count("hello world"))
print(count("python programming"))