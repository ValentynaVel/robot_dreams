# 2. Написати sql запит, який виведе кількість записів в табліці users, що старше 30 років.

import sqlite3
from pprint import pprint


query = (f'SELECT COUNT(*) FROM users WHERE age > 30')

conn = sqlite3.connect('database.sqlite')
cursor = conn.cursor()

res = cursor.execute(query)
pprint(res.fetchall())
