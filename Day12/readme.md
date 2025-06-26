# Day 12A: Count the Dots

### 🔹 Problem Statement  
Write a function called `count_dots` that takes a string as a parameter and returns the number of **dots (`.`)** in that string.

---

### ✏️ Examples

```python
count_dots("h.e.l.p.")    # Output: 4
count_dots("he.lp.")      # Output: 2
count_dots("hello")       # Output: 0
```
---
## ✅ Extra Challenge 12B: Your Age in Minutes

### 🔹 Problem Statement  
Write a function called `age_in_minutes` that prompts the user to enter their **year of birth**, validates the input, and returns their age in **minutes**.

---

### ⚠️ Input Validation Rules

Your code should continue asking the user for input until all of the following conditions are met:

1. ✅ The input must be exactly **4 digits**
2. ✅ The year must be **greater than or equal to 1900**
3. ✅ The year must be **less than or equal to the current year**

---

### 💡 How to Calculate Age in Minutes

Use the following formula:

```python
minutes = (current_year - year_of_birth) * 365 * 24 * 60
```
### ✏️ Example Interaction
```python
Enter your year of birth: 1930  
You are 48,355,200 minutes old.
```
### If the input is invalid:
```python
Enter your year of birth: 2500  
Please enter a valid 4-digit year between 1900 and 2025.
```