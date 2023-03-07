import sqlite3
import csv


# open the connection to the database
conn = sqlite3.connect('playstore_apps.db')
cur = conn.cursor()

# drop tables if they exist
conn.execute('DROP TABLE IF EXISTS app')
conn.execute('DROP TABLE IF EXISTS developer')
conn.execute('DROP TABLE IF EXISTS category')
conn.execute('DROP TABLE IF EXISTS ratings_reviews')

# create tables
conn.execute(
    '''CREATE TABLE developer (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        developer_uid TEXT, 
        developer_website TEXT, 
        developer_email TEXT)''')
conn.execute(
    '''CREATE TABLE category (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        category_name TEXT)''')
conn.execute(
    '''CREATE TABLE app (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        app_name TEXT, 
        app_identifier TEXT, 
        app_version TEXT, 
        app_size TEXT, 
        release_date TEXT, 
        rating_id INTEGER, 
        developer_id INTEGER,
        FOREIGN KEY (rating_id) REFERENCES ratings_reviews(id))''')
conn.execute(
    '''CREATE TABLE ratings_reviews (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        rating_count TEXT, 
        reviews INTEGER,
        app_id INTEGER,
        FOREIGN KEY (app_id) REFERENCES app(id))''')

# open the file to parse data and print to database
try:
    with open('playstore_dataset.csv', newline='', encoding="utf8") as r:
        reader = csv.reader(r, delimiter=",")
        next(reader)
        for row in reader:
            app_name = row[0]
            app_identifier = row[1]
            app_version = row[28]
            app_size = row[10]
            app_rating = row[3]
            release_date = row[15]
            developer_id = int(row[12])
            developer_uid = row[12]
            developer_website = row[13]
            developer_email = row[14]
            rating_count = row[4]
            reviews = row[23]
            category_name = row[2]
            try:
                cur.execute('INSERT INTO app VALUES (NULL,?,?,?,?,?,?,?)',
                            (app_name, app_identifier, app_version, app_size, release_date, app_rating, developer_id))

                app_id = cur.lastrowid

                cur.execute('INSERT INTO developer VALUES (NULL,?,?,?)',
                            (developer_uid, developer_website, developer_email))

                cur.execute('INSERT INTO ratings_reviews VALUES (NULL,?,?,?)',
                            (rating_count, reviews,app_id))


                cur.execute('INSERT INTO category VALUES (NULL,?)',
                            (category_name,))
            except sqlite3.IntegrityError as error:
                print("Error inserting row:", error)

            except Exception as e:
                print("Unexpected error:", error)
except:
    print("Unable to open .csv file")
finally:
    # commit changes and close connection
    conn.commit()
    conn.close()
