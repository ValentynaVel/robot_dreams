# 4. За допомогою flask_sqlalchemy підключити базу даних та створити такі моделі:
# User,
# Book,
# Purchase.
# Структура даних та звʼязки мають бути такими ж, як і в домашньому завданні до теми “Базова робота з базами даних. Part 2”.
# 1. Для обліку інформації про користувачів, книжки, видавництва та продажі створити наступні таблиці:
# user: id, first_name, last_name, age
# book: id, title, author, year, price
# purchase: id, user_id, book_id, date
# При цьому:
# user_id —  це FOREIGN KEY таблиці user
# book_id —  це FOREIGN KEY таблиці book

from __init__ import db


  class User(db.Model):
      id = db.Column(db.Integer, primary_key=True)
      first_name = db.Column(db.String)
      last_name = db.Column(db.String)
      age = db.Column(db.Integer, nullable=False)

     def __repr__(self):
         return f'My user {self.id}'

 class Book(db.Model):
     id = db.Column(db.Integer, primary_key=True)
     title = db.Column(db.String)
     author = db.Column(db.String)
     year = db.Column(db.Integer)
     price = db.Column(db.Integer)

     def __repr__(self):
         return f'My book {self.id}'

 class Purchase(db.Model):
     id = db.Column(db.Integer, primary_key=True)
     date = db.Column(db.String)
     user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
     user = db.relationship('User')
     book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
     book = db.relationship('Book')

     def __repr__(self):
         return f'My purchase {self.id}'





