def biggest_odd(numbers):
    odds=[int(n) for n in numbers if int(n)%2 !=0]
    return max(odds) if odds else "No odd digit"

print(biggest_odd("1234")) #3
print(biggest_odd("2468")) #No odd digit