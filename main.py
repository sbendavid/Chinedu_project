import sqlite3
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/app')
def application():
    try:
        # open the connection to the database
        conn = sqlite3.connect('playstore_apps.db')
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("""SELECT *  FROM app""")
        rows = cur.fetchall()
    except sqlite3.Error as error:
        # log error message and display to user
        print("Error connecting to the playstore database", error)
        return "Error connecting to the playstore database"
    finally:
        conn.close()

    return render_template('app.html', rows=rows)


@app.route('/developer')
def developer():
    try:
        # open the connection to the database
        conn = sqlite3.connect('playstore_apps.db')
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("""SELECT * FROM developer""")
        rows = cur.fetchall()
    except sqlite3.Error as error:
        # log error message and display to user
        print("Error connecting to the playstore database", error)
        return "Error connecting to the playstore database"
    finally:
        conn.close()
    return render_template('developer.html', rows=rows)


@app.route('/review')
def review():
    try:
        # open the connection to the database
        conn = sqlite3.connect('playstore_apps.db')
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("""SELECT ratings_reviews.*, app.app_rating
                        FROM ratings_reviews
                        JOIN app ON ratings_reviews.app_id = app.id
                    """)
        rows = cur.fetchall()
    except sqlite3.Error as error:
        # log error message and display to user
        print("Error connecting to the playstore database", error)
        return "Error connecting to the playstore database"
    finally:
        conn.close()

    return render_template('review.html', rows=rows)


@app.route('/app/<id>')
def ratings(id):
    try:
        conn = sqlite3.connect('playstore_apps.db')
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        # get results from customers
        cur.execute('SELECT * FROM ratings_reviews', [id])
        row = cur.fetchall()
        print(f"The rating for app {id} is {row}")
        print(row)
    except sqlite3.Error as error:
        # log error message and display to user
        print("Error retrieving app rating", error)
        return "Sorry, error retrieving app rating"
    finally:
        conn.close()
    return render_template('result.html', row=row)


if __name__ == '__main__':
    app.run(debug=True)
