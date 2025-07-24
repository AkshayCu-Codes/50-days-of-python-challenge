# 🔍 Day 48: Binary Search (Iterative)

## 🔹 Challenge Overview

Today's task is to **implement the Binary Search algorithm** to search for a number in a list. Binary search is an efficient algorithm for finding an item from a **sorted list** by repeatedly dividing the search interval in half.

---

## ✅ Problem Statement

Write a function called `search_binary` that:

- Takes **two parameters**:
  - `list1`: a list of numbers
  - `item`: the number to search for
- Uses the **binary search algorithm** (iterative method) to find the index of the `item` in `list1`
- Returns the **index** of the found item, or `-1` if the item is not found

---

## 🔢 Example Input

```python
list1 = [12, 34, 56, 78, 98, 22, 45, 13]
search_binary(list1, 22)
```
---
## 🚧 Important Note
Binary Search requires a sorted list. You will need to:

Sort the list first  
Then perform binary search

## 🧠 Concepts Practiced
Sorting a list  
Implementing binary search iteratively  
Returning index of a found element  

---

## 🧪 Expected Output
```python
Index of 22: 1
(Note: Output may vary depending on the sorted order)
```