import json
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        save_to_json('books.json', {'title': title, 'author': author})
        return 'Kniha byla přidána!'
    return render_template('add_book.html')

@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        save_to_json('users.json', {'username': username, 'email': email})
        return 'Uživatel přidán!'
    return render_template('add_user.html')

@app.route('/books')
def display_books():
    books = load_from_json('books.json')
    return render_template('books.html', items=books)

@app.route('/users')
def display_users():
    users = load_from_json('users.json')
    return render_template('users.html', items=users)

def save_to_json(filename, data):
    with open(filename, 'a') as file:
        json.dump(data, file)
        file.write('\n')

def load_from_json(filename):
    try:
        with open(filename, 'r') as file:
            return [json.loads(line) for line in file.readlines()]
    except FileNotFoundError:
        return []

if __name__ == '__main__':
    app.run(debug=True)
