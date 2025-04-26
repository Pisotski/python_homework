import os
import sqlite3

current_path = os.path.abspath(__file__)
root_path = current_path[
    : current_path.index("python_homework") + len("python_homework")
]
db_path = os.path.join(root_path, "db", "magazines.db")

with sqlite3.connect(db_path) as conn:
    conn.execute("PRAGMA foreign_keys = 1")
    cursor = conn.cursor()

    print("Database created and connected successfully.")

    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS Publishers (
        publisher_id INTEGER PRIMARY KEY,
        publisher_name TEXT NOT NULL UNIQUE
    )
    """
    )

    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS Subscribers (
        subscriber_id INTEGER PRIMARY KEY,
        subscriber_name TEXT NOT NULL,
        address TEXT NOT NULL
    )
    """
    )

    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS Magazines (
        magazine_id INTEGER PRIMARY KEY,
        magazine_title TEXT NOT NULL UNIQUE,
        publisher_id INTEGER,
        FOREIGN KEY (publisher_id) REFERENCES Publishers (publisher_id)
    )
    """
    )

    cursor.execute(
        """
    CREATE TABLE IF NOT EXISTS Subscriptions (
        subscription_id INTEGER PRIMARY KEY,
        subscriber_id INTEGER,
        magazine_id INTEGER,
        FOREIGN KEY (subscriber_id) REFERENCES Subscribers (subscriber_id),
        FOREIGN KEY (magazine_id) REFERENCES Magazines (magazine_id)
    )
    """
    )

    print("Tables created successfully.")
