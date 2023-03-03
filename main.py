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
    # cur.execute("""SELECT app_id_no, app.*, ratings_reviews.app_rating, app.release_date, developer.developer_uid  
    #             FROM app 
    #             LEFT JOIN ratings_reviews ON app.id = ratings_reviews.app_id
    #             LEFT JOIN developer ON app.developer_id = developer.id""")
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
    cur.execute("""SELECT * FROM ratings_reviews""")
    rows = cur.fetchall()

    conn.close()

    return render_template('review.html', rows=rows)

if __name__ == '__main__':
    app.run(debug=True)
