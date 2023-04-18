from __init__ import app
from flask import Flask, jsonify, request, redirect, abort, render_template
import random


@app.route('/hello')
def hello():
    app.logger.info('This is a request to `/hello`')
    return '<h1 style="color:red">Hello, world!</h1>'


app = Flask(__name__)

# 1.Створити функції для обробки таких запитів:
# GET/users – має повертати рандомний список імен (будь-яку кількість)
# GET/books – має повертати рандомний список книжок (будь-яку кількість) у вигляді html списку


# List of random users and books
random_users = ["Anna", "Bohdan", "Kristina", "Danil", "Emily", "Filip", "Gradzina", "Hanna", "Inna", "Volodymyr"]
random_books = ["Kobzar", "The Forest Song", "1984", "Eneida", "Stolen Happiness", "Shadows of the Forgotten Ancestors",
                "The Hobbit", "Marusia Churai", "Harry Potter", "Animal Farm"]

# Function to return a random list of names
@app.route('/users')
def get_users():
    return jsonify(random.sample(random_users, k=random.randint(1, 10)))

# Function to return a random list of books in HTML format
@app.route('/books')
def get_books():
    books_html = "<ul>"
    for book in random.sample(random_books, k=random.randint(1, 10)):
        books_html += "<li>" + book + "</li>"
    books_html += "</ul>"
    return books_html

# 2. Створити функції-обробники запитів на GET/users та GET/books, що мають приймати url-параметри
# (/users/1, /books/kobzar):
# Для /users – id, що може бути тільки числовим значенням. Якщо значення id ділиться на 2 - повертати текст із цим
# значенням. Якщо не ділиться – повертати статус 404 Not Found
# Для /books – title, текстове значення. Трансформувати першу літеру title у велику, а всі інші у маленькі (за допомогою
# одного із методів str), повернути трансформоване значення у якості відповіді


# Function to handle the /users endpoint with an id parameter
@app.route('/users/<int:user_id>')
def get_user_by_id(user_id):
    if user_id % 2 == 0:
        return f'<div>The user ID {user_id} is even.</div>'
    else:
        return 404


# Function to handle the /books endpoint with a title parameter
@app.route('/books/<string:title>')
def get_book_by_title(title):
    transformed_title = title.capitalize()
    return transformed_title

# 3. Створити функцію для обробки запитів GET /params – має повертати HTML таблицю, в якій будуть міститися ключі та
# значення query parameters.
# Наприклад, при запиті GET /params?name=Test&age=1, на сторінці має відобразитися:
# parameter | value
# name | Test
# age  | 1


@app.route('/params')
def process_params():
    params = request.args
    table_html = '<table><tr><th>parameter</th><th>value</th></tr>'
    for key, value in params.items():
        table_html += f'<tr><td>{key}</td><td>{value}</td></tr>'
    table_html += '</table>'
    return table_html


# 4. Створити функцію для обробки запитів GET, POST /login – при запиті GET має повертати HTML форму (method=POST,
# action=/login), що має містити поля username, password та кнопку submit.
# При запиті POST має перевіряти чи містяться в даних запиту username та password:
# Якщо запит містить ці дані, потрібно перенаправити користувача на сторінку /users.
# Якщо ні – потрібно повернути помилку 400 із інформацією про відсутні дані.


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username and password:
            return redirect('/users')
        else:
            abort(400, 'Missing username or password')

