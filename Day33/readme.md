# Day 33: List Intersection

### 🔹 Problem Statement  
Write a function called `inter_section` that:

- Takes **two lists** as parameters  
- Finds the **intersection** — the elements that appear in **both** lists  
- Returns the result as a **tuple**  
- Uses **list comprehension** in the solution

---

### 🧾 Lists to Use

```python
list1 = [20, 30, 60, 65, 75, 80, 85]
list2 = [42, 30, 80, 65, 68, 88, 95]
```

### ✏️ Example
```python
inter_section(list1, list2)
# Output: (30, 65, 80)
```
---

# Day 33 (Extra Challenge): Set or List

### 🔹 Problem Statement  
You want to write a program that searches for a number in a large range of values.  
The goal is to decide **whether a set or a list** performs the search operation faster.

You are given the following:

```python
a = range(10000000)
x = set(a)
y = list(a)
```

You're asked to search for a number 9999999 in both the set and the list.

Your task:  
1. Measure the time taken to search the number in each data structure
2. Compare performance
3. Decide whether a set or list is better for search operations
---
### ✅ Expected Output
Print the time taken by:

1. List lookup
2. Set lookup

Then print which one is faster and should be preferred for lookup tasks.