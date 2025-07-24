# 📊 Day 46: Create a DataFrame

## 🔹 Challenge Overview

In this challenge, you're tasked with using **Pandas**, a powerful Python data analysis library, to recreate a table by programmatically constructing a DataFrame.

---

## ✅ Problem Statement

Create a function or script that uses the **Pandas** library to recreate the table shown below as a DataFrame.

### 🎬 Input Data

| Year | Title      | Genre   |
|------|------------|---------|
| 2009 | Brothers   | Drama   |
| 2002 | Spider-Man | Sci-fi  |
| 2009 | WatchMen   | Drama   |
| 2010 | Inception  | Sci-fi  |
| 2009 | Avatar     | Fantasy |

---

## 🧾 Requirements

- Use the `pandas` library
- Define the data in Python (no external file import)
- Create a DataFrame using that data
- Print or return the DataFrame

---

## 🧠 Concepts Practiced

- Creating DataFrames using dictionaries or lists
- Column and row labeling
- Displaying structured data in tabular format

---

## 🔧 Example Output

```python
import pandas as pd

data = {
    'year': [2009, 2002, 2009, 2010, 2009],
    'Title': ['Brothers', 'Spider-Man', 'WatchMen', 'Inception', 'Avatar'],
    'genre': ['Drama', 'Sci-fi', 'Drama', 'Sci-fi', 'Fantasy']
}

df = pd.DataFrame(data)
print(df)
