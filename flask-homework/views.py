import json
import os
from __init__ import app, db
from flask import jsonify, request, redirect, abort, render_template, make_response, session, redirect, url_for
from models import User, Book, Purchase
import werkzeug.exceptions
import random


app.secret_key = os.getenv('SECRET_KEY') #add your secret key


@app.route('/hello')
def hello():
    app.logger.info('This is a request to `/hello`')
    return '<h1 style="color:red">Hello, world!</h1>'


# 1.Створити функції для обробки таких запитів:
# GET/users – має повертати рандомний список імен (будь-яку кількість)
# GET/books – має повертати рандомний список книжок (будь-яку кількість) у вигляді html списку


# Function to return a random list of names
# @app.route('/users')
# def get_users():
#     random_users = ["Anna", "Bohdan", "Kristina", "Danil", "Emily", "Filip", "Gradzina", "Hanna", "Inna", "Volodymyr"]
#     users = random.sample(random_users, k=random.randint(1, 10))
#     username = session.get('username')
#     if username:
#         return render_template('user_list.html', users=users)
#     else:
#         return redirect('/login')


# Function to return a random list of books in HTML format
# @app.route('/books')
# def get_books():
#     random_books = ["Kobzar", "The Forest Song", "1984", "Eneida", "Stolen Happiness",
#                     "Shadows of the Forgotten Ancestors",
#                     "The Hobbit", "Marusia Churai", "Harry Potter", "Animal Farm"]
#     books = random.sample(random_books, k=random.randint(1, 10))
#     username = session.get('username')
#     if username:
#         return render_template('books.html', books=books)
#     else:
#         return redirect('/login')

# 2. Створити функції-обробники запитів на GET/users та GET/books, що мають приймати url-параметри
# (/users/1, /books/kobzar):
# Для /users – id, що може бути тільки числовим значенням. Якщо значення id ділиться на 2 - повертати текст із цим
# значенням. Якщо не ділиться – повертати статус 404 Not Found
# Для /books – title, текстове значення. Трансформувати першу літеру title у велику, а всі інші у маленькі (за допомогою
# одного із методів str), повернути трансформоване значення у якості відповіді


# Function to handle the /users endpoint with an id parameter
# @app.route('/users/<int:user_id>')
# def get_user_by_id(user_id):
#     username = session.get('username')
#     if username:
#         if user_id % 2 == 0:
#             return render_template('user.html', user_id=user_id)
#         else:
#             return redirect('Bad Request', 400)
#     else:
#         return redirect('/login')


# Function to handle the /books endpoint with a title parameter
# @app.route('/books/<string:title>')
# def get_book_by_title(title):
#     transformed_title = title.capitalize()
#     username = session.get('username')
#     if username:
#         return render_template('book_title.html', title=transformed_title)
#     else:
#         return redirect('/login')


# 3. Створити функцію для обробки запитів GET /params – має повертати HTML таблицю, в якій будуть міститися ключі та
# значення query parameters.
# Наприклад, при запиті GET /params?name=Test&age=1, на сторінці має відобразитися:
# parameter | value
# name | Test
# age  | 1


@app.route('/params')
def params():
    if 'username' in session:
        username = session['username']
        return render_template('params.html', params=request.args, username=username)
    else:
        return redirect('/login')


# 4. Створити функцію для обробки запитів GET, POST /login – при запиті GET має повертати HTML форму (method=POST,
# action=/login), що має містити поля username, password та кнопку submit.
# При запиті POST має перевіряти чи містяться в даних запиту username та password:
# Якщо запит містить ці дані, потрібно перенаправити користувача на сторінку /users.
# Якщо ні – потрібно повернути помилку 400 із інформацією про відсутні дані.
# 2. В ендпоінт /login, при заповненні форми, додати функціонал запису імені користувача в сесію.


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        session['username'] = username
        password = request.form.get('password')
        if username and password:
            return redirect(url_for('current_user'))
        else:
            error = 'Missing username or password'
            return render_template('login.html', error=error)

@app.route('/cookies')
def cookies():
    return request.cookies, 200


@app.route('/current-user')
def current_user():
    current = session.get('username')
    if current:
        return f'<h1>Hello, {current}!</h1>'
    else:
        return redirect(url_for('/login'))


# 5. Модифікувати існуючі, або додати нові енпоінти. Дані відображати у форматі JSON або використовуючи HTML template:
# GET /users — відобразити список всіх обʼєктів User (всі записи відповідної таблиці)
# GET /users/<int:user_id> —- відобразити інформацію про User із відповідним id, або ж 404
# GET /books —- відобразити список всіх обʼєктів Book (всі записи відповідної таблиці)
# GET /books/<int:book_id> —- відобразити інформацію про Book із відповідним id, або ж 404
# GET /purchases —- відобразити список всіх обʼєктів Purchase (всі записи відповідної таблиці)
# GET /purchases/<int:purchase_id> —- відобразити інформацію про Purchase із відповідним id, або ж 404

 @app.route('/users')
 def users():
     dict_users = [
         {'id': user.id,
          'first_name': user.first_name,
          'second_name': user.second_name,
          'age': user.age} for user in users]
     return json.dumps(dict_users)


 @app.route('/users', methods=['POST', ])
 def create_user():
     user = User(
         first_name=request.json.get('fist_name'),
         last_name=request.json.get('last_name'),
         age=request.json.get('age')
     )
     db.session.add(user)
     db.session.commit()
     return f'User {user.id} created', 201


@app.route('/users/<int:user_id>')
def get_user_by_id():
    return render_template('users.html', user_id=user_id)


 @app.route('/books')
 def books():
     dict_books = [
         {'id': book.id,
          'title': book.title,
          'author': book.author,
          'year': book.year,
          'price': book.price,} for book in books]
     return json.dumps(dict_books)

@app.route('/books', methods=['POST', ])
 def create_book():
     book = Book(
         title=request.json.get('title'),
         author=request.json.get('author'),
         year=request.json.get('year'),
         price=request.json.get('price')
     )
     db.session.add(book)
     db.session.commit()
     return f'User {book.id} created', 201


@app.route('/purchases')
 def purchases():
     dict_purchases = [
         {'id': purchase.id,
          'date': purchase.date,
          'user_id': purchase.user_id,
          'book_id': purchase.book_id} for purchase in purchases]
     return json.dumps(dict_purchases)

@app.route('/purchases', methods=['POST', ])
 def create_purchase():
     purchase = Purchase(
         date=request.json.get('date'),
         user_id=request.json.get('user_id'),
         book_id=request.json.get('book_id')
         )
     db.session.add(purchase)
     db.session.commit()
     return f'Purchase {purchase.id} created', 201
