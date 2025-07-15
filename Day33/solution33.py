def inter_section(list1, list2):
    return tuple([item for item in list1 if item in list2])

# Example usage
list1 = [20, 30, 60, 65, 75, 80, 85]
list2 = [42, 30, 80, 65, 68, 88, 95]

print(inter_section(list1, list2))  # Output: (30, 65, 80)