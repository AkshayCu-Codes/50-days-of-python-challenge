# Day 29: Middle Figure

### 🔹 Problem Statement  
Write a function called `middle_figure` that takes **two string parameters**, `a` and `b`.  
The function should:

- Join the two strings together
- **Remove all whitespaces**
- Find the **middle character** of the combined string
- If the combined string has a middle character (odd length), return that character
- If the length is even, return `'no middle figure'`

---

### ✏️ Example

```python
middle_figure('make love', 'not wars')     
# Output: 'e'
```

### 🔍 Explanation:

Combined string: `'makelovenotwars'` → after removing whitespaces  
Length = 15 → odd → middle index = 7 → `'e'` is the middle character

---

### ✅ Expected Output

- A **single middle character** if length is odd  
- `'no middle figure'` if length is even
