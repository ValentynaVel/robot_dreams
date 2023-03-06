# Уявімо, що ми працюємо з інтернет-магазином, що займається продажем книжок.
# 1. Для обліку інформації про користувачів, книжки, видавництва та продажі створити наступні
# таблиці:
# users: id, first_name, last_name, age
# publishing_house: id, name, rating (default 5)
# books: id, title, author, year, price, publishing_house_id
# purchases: id, user_id, book_id, date
# При цьому:
# publishing_house_id — це FOREIGN KEY таблиці publishing_houses
# user_id —  це FOREIGN KEY таблиці users
# book_id —  це FOREIGN KEY таблиці books

import sqlite3
import time
from pprint import pprint


db = sqlite3.connect('database.sqlite')
curr = db.cursor()

users = ("CREATE TABLE IF NOT EXISTS users ("
               "id INTEGER PRIMARY KEY AUTOINCREMENT,"
               "first_name TEXT,"
               "last_name TEXT,"
               "age INTEGER NOT NULL)")

publishing_house = ("CREATE TABLE IF NOT EXISTS publishing_house ("
               "id INTEGER PRIMARY KEY AUTOINCREMENT,"
               "name TEXT,"
               "rating INTEGER DEFAULT 5)")

books = ("CREATE TABLE IF NOT EXISTS books ("
               "id INTEGER PRIMARY KEY AUTOINCREMENT,"
               "title TEXT,"
               "author TEXT,"
               "year INTEGER NOT NULL,"
               "price INTEGER,"
               "publishing_house_id INTEGER NOT NULL,"
               "FOREIGN KEY (publishing_house_id) references publishing_houses(id))")

purchases = ("CREATE TABLE IF NOT EXISTS purchases ("
               "id INTEGER PRIMARY KEY AUTOINCREMENT,"
               "user_id INTEGER NOT NULL,"
               "book_id INTEGER NOT NULL,"
               "date TEXT DEFAULT CURRENT_TIMESTAMP,"
               "FOREIGN KEY (user_id) references users(id),"
               "FOREIGN KEY (book_id) references books(id))")


curr.execute(users)
curr.execute(publishing_house)
curr.execute(books)
curr.execute(purchases)