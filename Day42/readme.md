# 📝 Day 42: Spelling Checker

## 🔹 Challenge Overview

Create a **spelling checker** using Python that detects and suggests corrections for misspelled words using the `TextBlob` library.

---

## ✅ Problem Statement

Write a function called `spelling_checker` that:

- Prompts the user to input a word.
- If the word is **misspelled**, the program should:
  - Suggest the correct spelling.
  - Ask: “Did you mean: `<suggested word>`? (yes/no)”
  - If the user responds **yes**, return the corrected word.
  - If the user responds **no**, prompt them to enter another word.
- If the input is correctly spelled, return it directly.

---

## 🔤 Example Interaction

```python
Enter a word: pythn
Did you mean: python? (yes/no): no
Enter a word: pytthon
Did you mean: python? (yes/no): yes
Correct word: python
```

---

## 🛠️ Requirements

- Use the `textblob` module
- Use a `while` loop for repeated prompting

---

## 💡 Tip

To install and configure `TextBlob`, use the following:

```bash
pip install textblob
python -m textblob.download_corpora
```