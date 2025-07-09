# Day 32: Password Validator

### 🔹 Problem Statement  
Write a function called `password_validator` that validates a user's password based on the following rules:

- Must be **at least 8 characters long**
- Must contain at least **one uppercase letter**
- Must contain at least **one lowercase letter**
- Must contain at least **one digit**

The function should:

- Prompt the user to enter a password  
- If the password is **valid**, return it  
- If the password is **not valid**, show the **specific validation errors**  
- Continue prompting the user until a valid password is entered (use a `while` loop)

---

### ✏️ Example

```python
Enter password: secret  
Error: Password must be at least 8 characters long  
Error: Password must contain at least one uppercase letter  
Error: Password must contain at least one digit  

Enter password: Secret123  
Password is valid!
```

### ✅ Expected Output
1. Validation feedback until a correct password is entered  
2. Final valid password is returned
