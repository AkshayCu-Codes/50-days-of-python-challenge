def odd_even(numbers):
    evens = [num for num in numbers if num%2==0]
    odds = [num for num in numbers if num%2!=0]

    if not evens or not odds:
        return "List must contain at least one even and one odd number."
    
    return max(evens) - min(odds)

print(odd_even([7, 3, 9, 12, 14]))