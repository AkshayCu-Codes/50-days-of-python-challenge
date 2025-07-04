# Day 22: Add Under_Score


### 🔹 Problem Statement  
Create **three functions**:

1. `add_hash` – Takes a string and adds a **hash (`#`)** between the words  
2. `add_underscore` – Takes the result from `add_hash` and **replaces all `#` with `_`**  
3. `remove_underscore` – Takes the result from `add_underscore` and **removes all `_`**

---

### ✏️ Example

```python
print(remove_underscore(add_underscore(add_hash('Python'))))  
# Output: 'Python'
