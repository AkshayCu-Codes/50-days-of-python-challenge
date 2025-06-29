def flat_list(nlist):
    result=[]
    for sublist in nlist:
        for item in sublist:
            result.append(item)
    return result

print(flat_list([[2, 4, 5, 6]]))         # Output: [2, 4, 5, 6]
print(flat_list([[1, 2], [3, 4]]))       # Output: [1, 2, 3, 4]
print(flat_list([[1], [2, 3], [4]]))     # Output: [1, 2, 3, 4]


# or

# def flat_list(nlist):
#     return [item for sublist in nlist for item in sublist]

