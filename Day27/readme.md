# Day 27: Unique Numbers

### 🔹 Problem Statement  
Write a function called `unique_numbers` that takes a **list of numbers** as an argument.

The function should:
- Find all the **unique numbers** in the list  
- Calculate the **sum of all numbers** in the original list  
- Calculate the **sum of unique numbers**  
- Find the **difference** between those two sums  
- If the difference is **even**, return the **original list**  
- If the difference is **odd**, return the list with **unique numbers only**

---

### ✏️ Example

```python
unique_numbers([1, 2, 4, 5, 6, 7, 8, 8])     
# Output: [1, 2, 4, 5, 6, 7, 8, 8]
```

### 🔍 Explanation:

- **Sum of original** = 41  
- **Sum of unique** = 33  
- **Difference** = 8 → Even → return original list

---

### ✅ Expected Output

Depending on the difference:

- **Even difference** → return original list  
- **Odd difference** → return list with only unique numbers
