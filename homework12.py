# 1. Створити базу даних SQLite. Використовуючи SQL запити, в створеній базі даних
# створити таблицю, яка має містити наступні поля:
# id - значення для кожного нового елементу має за замовчуванням бути +1 від попереднього
# first_name — текстове значення
# last_name — текстове значення
# age — число
# Формат здачі: Зберегти запит для створення таблиці в файл і запушити на git-репозиторій.

import sqlite3

db = sqlite3.connect('database.sqlite')
cursor = db.cursor()
query = ('CREATE TABLE IF NOT EXISTS users1 ('
         'id INTEGER PRIMARY KEY AUTOINCREMENT,'
         'first_name TEXT,'
         'second_name TEXT,'
         'age INTEGER)')

cursor.execute(query)

# 2. Створити SQL запити для додавання записів у створену таблицю. Створити запити для додавання
# мінімум 5 різних записів.
# Формат здачі: Запити зберегти в окремий файл і запушити на git-репозиторій

data = [
    ('Elon', 'Musk', 51),
    ('Elon', 'Musk', 52),
    ('Elon', 'Musk', 53),
    ('Elon', 'Musk', 54),
    ('Elon', 'Musk', 55),
]

query1 = ('INSERT INTO users1 (first_name, second_name, age) values (?, ?, ?)')

cursor.executemany(query1, data)
db.commit()



