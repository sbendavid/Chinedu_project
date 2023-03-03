import csv
import sqlite3

conn = sqlite3.connect('playstore_apps.db')
cur = conn.cursor()

conn.execute('DROP TABLE IF EXISTS app')
conn.execute('DROP TABLE IF EXISTS developer')
conn.execute('DROP TABLE IF EXISTS category')
conn.execute('DROP TABLE IF EXISTS ratings_reviews')

# print("table dropped successfully");

conn.execute(
    'CREATE TABLE developer (id INTEGER PRIMARY KEY AUTOINCREMENT, internal_id TEXT, website TEXT, developer_email TEXT)')
conn.execute('CREATE TABLE category (id INTEGER PRIMARY KEY AUTOINCREMENT, category_name TEXT)')
conn.execute(
    'CREATE TABLE app (id INTEGER PRIMARY KEY AUTOINCREMENT, app_name TEXT, app_identifier TEXT, app_version TEXT, app_size TEXT, release_date TEXT, app_rating REAL, developer_id INTEGER)')
conn.execute(
    'CREATE TABLE ratings_reviews (id INTEGER PRIMARY KEY AUTOINCREMENT, rating_count TEXT, reviews INTEGER)')

# print("table created successfully");

# open the file to print to database
with open('playstore_dataset.csv', newline='', encoding="utf8") as r:
    reader = csv.reader(r, delimiter=",")
    next(reader)
    for row in reader:
        # print(row)

        app_name = row[0]
        app_identifier = row[1]
        app_version = row[28]
        app_size = row[10]
        app_rating = row[3]
        release_date = row[14]
        developer_id = int(row[12])

        cur.execute('INSERT INTO app VALUES (NULL,?,?,?,?,?,?,?)',
                    (app_name, app_identifier, app_version, app_size, release_date, app_rating, developer_id))
        conn.commit()
# print("app data parsed successfully");

with open('playstore_dataset.csv', newline='', encoding="utf8") as r:
    reader = csv.reader(r, delimiter=",")
    next(reader)
    for row in reader:
        # print(row)

        developer_uid = row[12]
        developer_website = row[13]
        developer_email = row[13]

        cur.execute('INSERT INTO developer VALUES (NULL,?,?,?)', (developer_uid, developer_website, developer_email))
        conn.commit()
# print("developer data parsed successfully");

with open('playstore_dataset.csv', newline='', encoding="utf8") as r:
    reader = csv.reader(r, delimiter=",")
    next(reader)
    for row in reader:
        # print(row)

        rating_count = row[4]
        reviews = row[23]

        cur.execute('INSERT INTO ratings_reviews VALUES (NULL,?,?)', (rating_count, reviews))
        conn.commit()
# print("ratings data parsed successfully");

with open('playstore_dataset.csv', newline='', encoding="utf8") as r:
    reader = csv.reader(r, delimiter=",")
    next(reader)
    for row in reader:
        # print(row)

        category_name = row[2]

        cur.execute('INSERT INTO category VALUES (NULL,?)', (category_name,))
        conn.commit()
# print("category data parsed successfully")

conn.close()