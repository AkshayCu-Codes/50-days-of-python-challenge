import sqlite3

def create_connection():
    return sqlite3.connect("movies.db")

def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS movies (
            year INTEGER,
            title TEXT,
            genre TEXT
        )
    ''')
    
    conn.commit()
    conn.close()

def insert_data():
    movies = [
        (2009, "Brothers", "Drama"),
        (2002, "Spider Man", "Sci-fi"),
        (2009, "WatchMen", "Drama"),
        (2010, "Inception", "Sci-fi"),
        (2009, "Avatar", "Fantasy")
    ]
    
    conn = create_connection()
    cursor = conn.cursor()
    
    cursor.executemany("INSERT INTO movies (year, title, genre) VALUES (?, ?, ?)", movies)
    
    conn.commit()
    conn.close()

def view_all_movies():
    conn = create_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM movies")
    movies = cursor.fetchall()
    
    conn.close()
    return movies

def select_movie_by_title(title):
    conn = create_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM movies WHERE title=?", (title,))
    movie = cursor.fetchall()
    
    conn.close()
    return movie

def select_movies_by_year(year):
    conn = create_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM movies WHERE year=?", (year,))
    movies = cursor.fetchall()
    
    conn.close()
    return movies

def select_movies_by_genre(genres):
    conn = create_connection()
    cursor = conn.cursor()
    
    query = "SELECT * FROM movies WHERE genre IN ({})".format(",".join("?" * len(genres)))
    cursor.execute(query, genres)
    movies = cursor.fetchall()
    
    conn.close()
    return movies

def delete_all_movies():
    conn = create_connection()
    cursor = conn.cursor()
    
    cursor.execute("DELETE FROM movies")
    
    conn.commit()
    conn.close()


# ------------------------------
# Run all functions step-by-step
# ------------------------------
create_table()
insert_data()

print("\n🎬 All Movies:", view_all_movies())
print("\n🎯 Movie - Brothers:", select_movie_by_title("Brothers"))
print("\n📅 Movies in 2009:", select_movies_by_year(2009))
print("\n🎭 Movies in Fantasy & Drama:", select_movies_by_genre(["Fantasy", "Drama"]))

delete_all_movies()
print("\n🗑️ After Deletion:", view_all_movies())