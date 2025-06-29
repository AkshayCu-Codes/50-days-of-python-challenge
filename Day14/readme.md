
# Day 14: Flatten the List & Teacher's Salary

This file documents the coding tasks completed for **Day 14**.

---

## ✅ Challenge 14A: Flatten the List

### 🔹 Problem Statement  
Write a function called `flat_list` that takes one argument — a **nested list** — and returns a **one-dimensional list**.

### ✏️ Example

```python
flat_list([[2, 4, 5, 6]])           # Output: [2, 4, 5, 6]
flat_list([[1, 2], [3, 4]])         # Output: [1, 2, 3, 4]
flat_list([[1], [2, 3], [4]])       # Output: [1, 2, 3, 4]
```

### ✅ Output  
The function returns a flat list containing all the elements from the nested list.

---

## ✅ Extra Challenge 14B: Teacher’s Salary

### 🔹 Problem Statement  
Write a function called `your_salary` that:

- Asks the user to input:
  - The **teacher's name**
  - The **number of periods** taught in a month

- Calculates the gross monthly salary:
  - For the first 100 periods → $20 per period
  - For every period above 100 → $25 per period

### ✏️ Example

```
Enter teacher's name: John Kelly
Enter periods taught: 105

Teacher: John Kelly
Periods: 105
Gross salary: 2,125
```

### ✅ Output Format

```
Teacher: <name>
Periods: <number>
Gross salary: <amount>
```
