# 2. Написати запит, який виведе дату покупки і імʼя користувача, що її здійснив.
# Результат має бути представлений у форматі: purchases.id, purchases.date, user.first_name,
# user.last_name
#
import sqlite3
from pprint import pprint

conn = sqlite3.connect('database.sqlite')
curr = conn.cursor()

query = ('SELECT purchases.id, purchases.date, users.first_name, users.last_name'
         ' FROM purchases JOIN users ON purchases.user_id = users.id')


res = curr.execute(query)
pprint(res.fetchall())

