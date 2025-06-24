# Day 10: Hide My Password + Thousand Separator (Extra Challenge)

---

## ✅ Challenge A: Hide My Password

### 🧩 Problem  
Write a function called `hide_password` that takes no parameters.  
The function should:
- Ask the user to enter a password using `input()`
- Replace all characters in the password with `*`
- Print the hidden password and its length

---

### ✏️ Example

```python
Input: hello
Output: *****
        Your password is 5 characters long
```
---

## ✅ Challenge B: Thousand Separator

### 🧩 Problem  
You are given a list of large numbers without any formatting.  
Write a function called `convert_numbers` that takes a **list of integers** as input and returns a **list of strings**, where:

- Each number is **converted into a string**
- Each string has **commas as thousand separators** for better readability

---

### ✏️ Example

```python
Input: [1000000, 2356989, 2354672, 9878098]

Output: ['1,000,000', '2,356,989', '2,354,672', '9,878,098']