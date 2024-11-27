import sqlite3


conn = sqlite3.connect("school.db")
cursor = conn.cursor()

conn = sqlite3.connect("school.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS countries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL
)
""")
conn.commit()

cursor.executemany("""
INSERT INTO countries (title) VALUES (?)
""", [("Кыргызстан",), ("Германия",), ("Китай",)])
conn.commit()

cursor.execute("""
CREATE TABLE IF NOT EXISTS cities (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    area REAL DEFAULT 0,
    country_id INTEGER NOT NULL,
    FOREIGN KEY (country_id) REFERENCES countries(id)
)
""")
conn.commit()

cursor.executemany("""
INSERT INTO cities (title, area, country_id) VALUES (?, ?, ?)
""", [
    ("Бишкек", 127.0, 1),
    ("Ош", 182.0, 1),
    ("Берлин", 891.8, 2),
    ("Чунцин", 310.7, 2),
    ("Ухань", 16410.54, 3),
    ("Сиань", 6340.5, 3),
    ("Гуанчжоу", 7434.4, 3)
])
conn.commit()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    city_id INTEGER NOT NULL,
    FOREIGN KEY (city_id) REFERENCES cities(id)
)
""")
conn.commit()

cursor.executemany("""
INSERT INTO students (first_name, last_name, city_id) VALUES (?, ?, ?)
""", [
    ("Адина", "Иманалиева", 1),
    ("Бекжон", "Токтосунов", 1),
    ("Аливия", "Баймуратова", 2),
    ("Канат", "Асаманов", 2),
    ("Лукас", "Мюллер", 3),
    ("Ханна", "Шуль", 3),
    ("Марио", "Вагн", 4),
    ("Клара", "Фишер", 4),
    ("Ле", "Вэй", 5),
    ("Чен", "Хуан", 5),
    ("Мэй", "Юй", 6),
    ("Юу", "Чан", 6),
    ("Юн", "Ли", 7),
    ("Дан", "Лу", 7),
    ("Нуржан", "Абдрахманов", 1)
])
conn.commit()

def get_cities():
    cursor.execute("SELECT id, title FROM cities")
    return cursor.fetchall()

def get_students_by_city(city_id):
    cursor.execute("""
        SELECT 
            students.first_name,
            students.last_name,
            countries.title AS country,
            cities.title AS city,
            cities.area
        FROM students
        JOIN cities ON students.city_id = cities.id
        JOIN countries ON cities.country_id = countries.id
        WHERE cities.id = ?
    """, (city_id,))
    return cursor.fetchall()

def close_connection():
    conn.close()