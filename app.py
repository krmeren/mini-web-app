from flask import Flask, render_template, request, redirect
import sqlite3
import os

app = Flask(__name__)

# Veritabanı yolu (container içinde /app/data/users.db)
DB_PATH = os.path.join(os.path.dirname(__file__), 'data', 'users.db')

# Veritabanını başlat
def init_db():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL
                )''')
    conn.commit()
    conn.close()

# Ana sayfa - isim ekleme
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        if name.strip():  # Boş girişi engelle
            conn = sqlite3.connect(DB_PATH)
            c = conn.cursor()
            c.execute('INSERT INTO users (name) VALUES (?)', (name,))
            conn.commit()
            conn.close()
        return redirect('/list')
    return render_template('index.html')

# Liste sayfası - kayıtları göster
@app.route('/list')
def list_users():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('SELECT * FROM users')
    users = c.fetchall()
    conn.close()
    return render_template('list.html', users=users)

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000)
