# Day 39: Password Generator

### 🔹 Problem Statement  
Write a function called `generate_password` that:

- Asks the user how strong they want their password:
  - `"weak"` → 5 characters  
  - `"strong"` → 8 characters  
  - `"very strong"` → 12 characters
- Generates a **random password** of the specified strength
- The password should include a mix of:
  - **Uppercase letters**
  - **Lowercase letters**
  - **Digits**
  - **Punctuation symbols**

---

### ✏️ Example

```python
generate_password()
# User input: strong
# Output: a randomly generated password with 8 characters like "F5#kW2z!"
```

### ✅ Expected Output
A secure, random password with the requested strength.