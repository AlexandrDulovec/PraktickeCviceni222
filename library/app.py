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
        save_to_file('books.txt', f"Nadpis knihy: {title}, Autor: {author}")
        return 'Kniha byla přidána!'
    return render_template('add_book.html')

@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        save_to_file('users.txt', f"Uživatelské jméno: {username}, Email: {email}")
        return 'Uživatel přidán!'
    return render_template('add_user.html')

def save_to_file(filename, data):
    with open(filename, 'a') as file:
        file.write(data + '\n')

if __name__ == '__main__':
    app.run(debug=True)
