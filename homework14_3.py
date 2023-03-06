# 3. Написати запит, який виведе всіх users і назви  всіх книжок, які вони купували,
# відсортувати дані за user_id.
# Результат має бути представлений у форматі: users.id, users.first_name, users.last_name,
# books.title

import sqlite3
from pprint import pprint

conn = sqlite3.connect('database.sqlite')
curr = conn.cursor()

query = ('SELECT users.id, users.first_name, users.last_name, books.title'
         ' FROM users '
         'JOIN purchases ON purchases.user_id = users.id'
         ' JOIN books ON purchases.book_id = books.id')


res = curr.execute(query)
pprint(res.fetchall())