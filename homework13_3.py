# 3. Написати sql запит, який виведе інформацію про вік (кількість років) та кількість
# користувачів, які відповідають цьому віку. Результатом виконання такого запиту має
# бути таблиця:

    # age  | users
    # 32    | 1
    # 52    | 2
    # 120  | 2
    # 1142 | 1

import sqlite3
from pprint import pprint

conn = sqlite3.connect('database.sqlite')
cursor = conn.cursor()

query = ("SELECT age, COUNT(id) as users FROM users GROUP BY age")


res = cursor.execute(query)
pprint(res.fetchall())
