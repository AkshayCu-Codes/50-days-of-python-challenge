# Day 40: Pig Latin

### 🔹 Problem Statement  
Write a function called `translate` that takes a sentence and converts it into **Pig Latin** using the following rules:

#### ✅ Rules:
1. If a word starts with a **vowel** (`a, e, i, o, u`), add `'yay'` at the end of the word  
   👉 For example: `'eat'` becomes `'eatyay'`
2. If a word starts with a **consonant**, move the **first letter** to the end and add `'ay'`  
   👉 For example: `'day'` becomes `'ayday'`

---

### 🔤 Example Input

```python
a = "i love python"
translate(a)
```
---
### ✅ Expected Output
```python
"iyay ovelay ythonpay"
```
Each word in the sentence is converted individually and joined to form the Pig Latin sentence.