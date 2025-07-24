# 📅 Day 49: Create a Movie Database using SQLite

## 🔹 Challenge Overview

In today’s challenge, you’ll use **SQLite with Python** to build a mini movie database. You will create a table, insert data, and run SQL operations to query and manage your dataset.

---

## ✅ Problem Statement

Create a database called `movies.db` using Python’s built-in `sqlite3` module.

### Your tasks:

1. Create a **table** called `movies` with the following columns:
   - `year` (INTEGER)
   - `title` (TEXT)
   - `genre` (TEXT)

2. **Insert the following data** into the `movies` table:

| year | title      | genre   |
|------|------------|---------|
| 2009 | Brothers   | Drama   |
| 2002 | Spider Man | Sci-fi  |
| 2009 | WatchMen   | Drama   |
| 2010 | Inception  | Sci-fi  |
| 2009 | Avatar     | Fantasy |

---

## 🔍 SQL Operations to Perform

Once the data is inserted, perform the following SQL queries from your Python script:

- View all movies in the table.
- Select only the movie **"Brothers"**.
- Select all movies that were released in **2009**.
- Select all movies in the **Fantasy** and **Drama** genres.
- Delete all contents from the `movies` table.

---

## 📦 Requirements

- Use Python’s `sqlite3` module
- Store the database as a local file (`movies.db`)
- Make sure to `commit()` changes and `close()` your connection after transactions

---

## 💡 Bonus

Try adding exception handling to gracefully manage database connection errors or SQL syntax issues.

---

## 🧠 What You’ll Learn

- Basics of working with relational databases in Python
- Creating tables and inserting records in SQLite
- Writing and executing SQL commands through Python
- Managing and querying datasets effectively

---

