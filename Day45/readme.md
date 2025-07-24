# 📝 Day 45: Words and Special Characters

## 🔹 Challenge Overview

In this challenge, you’ll analyze a string to identify and count different elements such as **words**, **special characters**, and the **total number of characters** (excluding whitespace).

---

## ✅ Problem Statement

Write a function called `analyse_string` that takes a string as input and returns a dictionary with the following details:

- `"special character"`: Total count of special characters in the string  
- `"words"`: Total number of words in the string  
- `"total characters"`: Total number of non-whitespace characters (letters + digits + punctuation)

---

### 📥 Input

A string like:
```text
Python has a string format operator %. This functions analogously to
printf format strings in C, e.g. "spam=%s eggs=%d" % ("blah", 2)
evaluates to "spam=blah eggs=2".

Source Wikipedia.  
```
---
✅ Expected Output
A dictionary in this format:

```python
{
  "special character": 17,
  "words":  thirty-five,
  "total characters": 172
}
```
(Note: The actual values are just illustrative — your function should calculate them.)
---

