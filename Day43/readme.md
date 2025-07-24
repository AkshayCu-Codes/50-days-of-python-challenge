# 📘 Day 43: Student Marks

## 🔹 Challenge Overview

Create a simple Python function that records student names along with their marks and stores them in a dictionary. This challenge helps practice loops, input handling, and dictionary usage.

---

## ✅ Problem Statement

Write a function called `student_marks` that:

- Asks the user to input a **student's name**
- Then prompts for the **marks** achieved by that student
- Stores this data in a dictionary where:
  - Key = Student's name
  - Value = Marks
- Repeats this process until the user types `done`
- Returns the final dictionary of all students and their marks

---

## 🔤 Example Interaction
```python
Enter student name: Alice
Enter marks: 89
Enter student name: Bob
Enter marks: 76
Enter student name: done

{'Alice': 89, 'Bob': 76}
```

---

## 🧠 Concepts Practiced

- User input and loops
- Dictionary creation and updating
- Sentinel values (`done`) to end input loop

---

## 💡 Tips

- Ensure marks are stored as **integers** or **floats**.
- Be sure to **check for the "done" keyword** to break out of the loop.
