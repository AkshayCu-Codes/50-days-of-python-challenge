def sum_list(nlist):
    sum=0
    for sublist in nlist:
        for item in sublist:
            sum += item
    return sum

print(sum_list([[2, 4, 5, 6], [2, 3, 5, 6]]))  # Output: 33
print(sum_list([[1], [2, 3], [4]]))           # Output: 10
print(sum_list([[10, 20], [30], [5, 5]]))     # Output: 70



# or

# def sum_list(nlist):
#     return sum(item for sublist in nlist for item in sublist)

