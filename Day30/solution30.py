def repeated_name(names):
    counts={}
    for name in names:
        if name in counts:
            counts[name] += 1
        else:
            counts[name] = 1

    print(counts)

    max_count=0
    most_repeated=""
    for name , count in counts.items():
        if count>max_count:
            max_count=count
            most_repeated=name
    return most_repeated

print(repeated_name(["john","peter","john"]))
print(repeated_name(["John", "Peter", "John", "Peter", "Jones", "Peter"]))