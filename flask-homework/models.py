# 4. За допомогою flask_sqlalchemy підключити базу даних та створити такі моделі:
# User,
# Book,
# Purchase.
# Структура даних та звʼязки мають бути такими ж, як і в домашньому завданні до теми “Базова робота з базами даних. Part 2”.
# 1. Для обліку інформації про користувачів, книжки, видавництва та продажі створити наступні таблиці:
# user: id, first_name, last_name, age
# publishing_house: id, name, rating (default 5)
# book: id, title, author, year, price, publishing_house_id
# purchase: id, user_id, book_id, date
# При цьому:
# publishing_house_id — це FOREIGN KEY таблиці publishing_house
# user_id —  це FOREIGN KEY таблиці user
# book_id —  це FOREIGN KEY таблиці book

from __init__ import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    age = db.Column(db.Integer, nullable=False)


class Publishing_house(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    rating = db.Column(db.Integer)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    author = db.Column(db.String)
    year = db.Column(db.Integer)
    price = db.Column(db.Integer)
    publishing_house_id = db.Column(db.Integer, db.ForeignKey('publishing_house.id'), nullable=False)
    publishing_house = db.relationship('Publishing_house')


class Purchase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User')
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)
    book = db.relationship('Book')
    date = db.Column()
