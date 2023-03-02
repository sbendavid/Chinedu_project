DROP TABLE IF EXISTS app;
DROP TABLE IF EXISTS developer;
DROP TABLE IF EXISTS category;
DROP TABLE IF EXISTS ratings_reviews;

print("table dropped successfully");

CREATE TABLE app (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    app_name TEXT, 
    app_version TEXT, 
    app_size TEXT, 
    category_id INTEGER, 
    developer_id INTEGER, 
    FOREIGN KEY(category_id) REFERENCES category(id), 
    FOREIGN KEY(developer_id) REFERENCES developer(id)
);
CREATE TABLE developer (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    developer_uid TEXT, 
    developer_website TEXT, 
    developer_email TEXT
);
CREATE TABLE category (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    name TEXT
);
CREATE TABLE ratings_reviews (
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    app_id INTEGER, 
    app_rating TEXT, 
    rating_count TEXT, 
    reviews INTEGER, 
    FOREIGN KEY(app_id) REFERENCES app(id)
);


INSERT INTO app (app_name, app_version, app_size, category_id, developer_id)
VALUES (1, 'My App 1', 1, 1, 1.99);

INSERT INTO developer (app_id, app_name, category_id, developer_id, price)
VALUES (2, 'My App 2', 2, 2, 0.99);

INSERT INTO category (app_id, app_name, category_id, developer_id, price)
VALUES (3, 'My App 3', 1, 1, 2.99);

INSERT INTO ratings_reviews (app_id, app_name, category_id, developer_id, price)
VALUES (3, 'My App 3', 1, 1, 2.99);

print("table created successfully");
