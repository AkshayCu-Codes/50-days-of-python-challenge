# 📧 Day 44: Save Emails

## 🔹 Challenge Overview

This challenge focuses on reading from and writing to CSV files using Python. You’ll create two functions: one for saving user-input emails and another for reading them back.

---

## ✅ Problem Statement

### Function 1: `save_emails()`
- Prompts the user to input **email addresses** one by one.
- Continues accepting input until the user types `"done"`.
- Saves each email on a **new line** in a CSV file (`emails.csv`).
- Closes the file once done.

### Function 2: `open_emails()`
- Opens the `emails.csv` file.
- Reads and displays all saved emails, each on a new line.

---

## 🔤 Example Interaction

### Sample Input to `save_emails()`:
```python
Enter email: jj@gmail.com
Enter email: kate@yahoo.com
Enter email: done
```

### `emails.csv` output:
```
jj@gmail.com
kate@yahoo.com
```

### Output of `open_emails()`:
```
jj@gmail.com
kate@yahoo.com
```

## 🧠 Concepts Practiced

- File handling with Python (`open`, `write`, `read`)
- CSV formatting basics
- Loops and user input
- String manipulation and newline characters

---

## 💡 Tips

- Use `'a'` mode in `open()` to **append** emails if the file already exists.
- Ensure each email ends with a **newline character (`\n`)** when writing to the file.
- Handle edge cases like empty input or duplicate entries if needed.

---