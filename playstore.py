import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # open the connection to the database
    conn = sqlite3.connect('playstore_apps.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("select * from app")
    rows = cur.fetchall()
    conn.close()
    return render_template('index.html', rows=rows)

# @app.route('/application/<id>')
# def ratings(id):
#     conn = sqlite3.connect('playstore_apps.db')
#     conn.row_factory = sqlite3.Row
#     cur = conn.cursor()
#     # get results from customers
#     app_id = 1  # replace with the ID of the app you want to see the rating for
#     cur.execute('SELECT app_rating FROM ratings_reviews WHERE app_id = ?', (app_id,))
#     rating = cur.fetchone()[0]
#     print(f"The rating for app {app_id} is {rating}")
#     conn.close()
#     return render_template('application.html', customer=customer)


@app.route('/developer')
def developer():
    # open the connection to the database
    conn = sqlite3.connect('playstore_apps.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("select * from developer")
    rows = cur.fetchall()
    conn.close()
    return render_template('developer.html', rows=rows)

