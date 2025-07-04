# Day 23: Simple Calculator


### 🔹 Problem Statement  
Create a **simple calculator** that performs basic math operations:

- Addition (`+`)
- Subtraction (`-`)
- Multiplication (`*`)
- Division (`/`)

The calculator should:

- Take **user input** for the operation and numbers
- Perform the operation
- Handle the following exceptions:
  - `ZeroDivisionError` – when dividing by zero
  - `ValueError` – if input is not a valid number
  - `NameError` – if invalid input causes undefined variable usage

---

### ✏️ Example

```python
# Input
Enter first number: 10  
Enter operator (+, -, *, /): /  
Enter second number: 2  

# Output
Result: 5.0
