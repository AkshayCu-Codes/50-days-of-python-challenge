# Day 38: Guess a Number

### 🔹 Problem Statement  
Write a function called `guess_a_number` that:

- **Generates a random number** between 1 and 10  
- Asks the user to **guess the number**  
- Tells the user if their guess is **too high** or **too low**  
- The user gets a **maximum of 3 guesses**

---

### 🧠 Game Logic

- If the user guesses correctly within 3 tries → print: `"You win!"`  
- If the user fails after 3 tries → print: `"You lose! The number was X"`

---

### ✏️ Example

```python
guess_a_number()
# Output (example):
# Guess a number between 1 and 10: 7
# Too low!
# Guess a number between 1 and 10: 9
# Too high!
# Guess a number between 1 and 10: 8
# You win!
```
### ✅ Expected Output
- Feedback for each guess (Too high!, Too low!)  
- A win/loss message after 1 to 3 attempts