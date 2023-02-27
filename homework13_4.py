# 4. Написати sql запит, який буде робити те саме, що і в завданні 3, але виводити дані
# відсортовані по кількості користувачів у спадаючому порядку та по віку у зростаючому
# порядку. Результатом має бути таблиця:
    # age  | users
    # 52    | 2
    # 120  | 2
    # 32    | 1
    # 1142 | 1

import sqlite3
from pprint import pprint

conn = sqlite3.connect('database.sqlite')
cursor = conn.cursor()

query = ("SELECT age, COUNT(id) as users FROM users GROUP BY age ORDER BY users desc, age")


res = cursor.execute(query)
pprint(res.fetchall())