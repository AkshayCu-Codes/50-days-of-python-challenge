# Day 11: Are They Equal?

---

## ✅ Challenge

### 🧩 Problem  
Write a function called `equal_strings` that takes **two strings** as arguments and compares them.

The function should:
- Return `True` if the two strings:
  - Have the **same characters**, and
  - Are of **equal length** (i.e., anagrams)
- Return `False` otherwise

---

### ✏️ Example

```python
equal_strings('love', 'evol')     # True
equal_strings('python', 'typhon') # True
equal_strings('hello', 'helloo')  # False
equal_strings('abc', 'def')       # False
