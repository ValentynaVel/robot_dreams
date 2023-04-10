# 1. Написати sql запит, який вибере усі записи із таблиці users старше
# 30 років.

import sqlite3
from pprint import pprint


query = (f'SELECT * FROM users WHERE age > 30')

conn = sqlite3.connect('database.sqlite')
cursor = conn.cursor()

res = cursor.execute(query)
pprint(res.fetchall())