def search_binary(list1, item):
    # Step 1: Sort the list
    sorted_list = sorted(list1)
    
    # Step 2: Binary Search (Iterative)
    low = 0
    high = len(sorted_list) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if sorted_list[mid] == item:
            return mid  # Return index in sorted list
        elif sorted_list[mid] < item:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1  # Item not found


# Example Usage
list1 = [12, 34, 56, 78, 98, 22, 45, 13]
index = search_binary(list1, 22)
print(f"Index of 22: {index}")