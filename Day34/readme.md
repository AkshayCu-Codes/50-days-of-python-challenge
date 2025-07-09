# Day 34: Just Digits

### 🔹 Problem Statement  
You are given a block of text.  
Copy the text below and **save it as a CSV file** named `python.csv` in the **same folder** as your Python file.

---

### 📝 CSV Text (Save this as `python.csv`)

Python was released in 1991 for the first time. Python 2 was
released in 2000 and introduced new features, such as list
comprehensions and a cycle-detecting garbage collection system
(in addition to reference counting). Python 3 was released in 2008
and was a major revision of the language that is not
completely backward-compatible.


---

### 🔧 Task  
Write a function called `just_digits` that:

- **Reads** the text from the CSV file  
- **Extracts only digit elements** from the file  
- **Returns a list of digits** as **strings**

---

### ✏️ Example

```python
just_digits()
# Output: ['1991', '2', '2000', '3', '2008']
```
### ✅ Expected Output  
A list of all numbers found in the text in the order they appear.
Each number should be a string.

