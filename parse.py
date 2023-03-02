import csv
import sqlite3

conn = sqlite3.connect('playstore_apps.db')
cur = conn.cursor()

conn.execute('DROP TABLE IF EXISTS app')
conn.execute('DROP TABLE IF EXISTS developer')
conn.execute('DROP TABLE IF EXISTS category')
conn.execute('DROP TABLE IF EXISTS ratings_reviews')

print("table dropped successfully");

conn.execute('CREATE TABLE developer (id INTEGER PRIMARY KEY AUTOINCREMENT, developer_uid TEXT, developer_website TEXT, developer_email TEXT)')
conn.execute('CREATE TABLE category (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)')
conn.execute('CREATE TABLE app (id INTEGER PRIMARY KEY AUTOINCREMENT, app_name TEXT, app_version TEXT, app_size TEXT, category_id INTEGER, developer_id INTEGER, FOREIGN KEY(category_id) REFERENCES category(id), FOREIGN KEY(developer_id) REFERENCES developer(id))')
conn.execute('CREATE TABLE ratings_reviews (id INTEGER PRIMARY KEY AUTOINCREMENT, app_id INTEGER, app_rating TEXT, rating_count TEXT, reviews INTEGER, FOREIGN KEY(app_id) REFERENCES app(id))')

print("table created successfully");

# open the file to print to database
with open('playstore_dataset.csv', newline='', encoding="utf8") as r:
    reader = csv.reader(r, delimiter=",")
    next(reader)
    for row in reader:
        print(row)

        app_name = row[0]
        #app_id = row[1]
        app_version = row[28]
        app_size = row[10]
        app_rating = row[3]
        release_date = row[14]
        developer_uid = row[12]
        developer_website = row[13]
        developer_email = row[13]
        rating_count = row[4]
        reviews = row[23]
        category_name = row[2]

        cur.execute('INSERT INTO app VALUES (NULL,?,?,?,?,?)',(app_name, app_version, app_size, None, None))
        app_id = cur.lastrowid
        cur.execute('INSERT INTO developer VALUES (NULL,?,?,?)', (developer_uid, developer_website, developer_email))
        developer_id = cur.lastrowid
        cur.execute('INSERT INTO category VALUES (NULL,?)', (category_name,))
        category_id = cur.lastrowid
        cur.execute('INSERT INTO ratings_reviews VALUES (NULL,?,?,?,?)', (app_id, app_rating, rating_count, reviews))

    print("data parsed successfully");
    conn.commit()
    conn.close()