# 📦 Day 47: Save a JSON

## 🔹 Challenge Overview

Today’s challenge is all about **JSON** – the most widely used format for storing and exchanging data. You'll practice how to **write a Python dictionary to a JSON file** and how to **read it back**.

---

## ✅ Problem Statement

Create two functions:

1. **`save_json(data)`**  
   - Accepts a dictionary as an argument.  
   - Saves the dictionary into a file in **JSON** format.

2. **`read_json()`**  
   - Opens the previously saved JSON file.  
   - Reads and prints or returns its content.

---

## 🎯 Input Dictionary

Use the dictionary below as input to the `save_json` function:

```python
names = {
    'name': 'Carol',
    'sex': 'female',
    'age': 55
}
```
---

## 📦 Expected Output
```python
{'name': 'Carol', 'sex': 'female', 'age': 55}
```