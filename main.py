import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/app')
def application():

    # open the connection to the database
    conn = sqlite3.connect('playstore_apps.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("""SELECT *  FROM app""")
    rows = cur.fetchall()

    conn.close()

    return render_template('app.html', rows=rows)

@app.route('/developer')
def developer():

    # open the connection to the database
    conn = sqlite3.connect('playstore_apps.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("""SELECT * FROM developer""")
    rows = cur.fetchall()

    conn.close()

    return render_template('developer.html', rows=rows)

@app.route('/review')
def review():

    # open the connection to the database
    conn = sqlite3.connect('playstore_apps.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("""SELECT ratings_reviews.*, app.app_rating
                    FROM ratings_reviews
                    JOIN app ON ratings_reviews.app_id = app.id
                """)
    rows = cur.fetchall()

    conn.close()

    return render_template('review.html', rows=rows)

@app.route('/app/<id>')
def ratings(id):
    conn = sqlite3.connect('playstore_apps.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    # get results from customers
    cur.execute('SELECT app_rating FROM app WHERE app_id = ?', (id,))
    rating = cur.fetchone()[1]
    print(f"The rating for app {id} is {rating}")
    conn.close()
    return render_template('result.html', rating=rating)

if __name__ == '__main__':
    app.run(debug=True)
