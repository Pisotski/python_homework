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

# Create functions, one for each of the tables, to add entries.
# Include code to handle exceptions as needed, and to ensure that there is
# no duplication of information.
# The subscribers name and address columns don't have unique values --
# you might have several subscribers with the same name --
# but when creating a subscriber you should check that you don't already
# have an entry where BOTH the name and the address are the same as for
# the one you are trying to create.


def add_publisher(cursor, publisher_name):
    try:
        cursor.execute(
            "INSERT INTO Publishers (publisher_name) VALUES (?)", (publisher_name,)
        )
    except sqlite3.IntegrityError:
        print(f"{publisher_name} is already in the database.")


def add_magazine(cursor, magazine_title, publisher_name):
    try:
        cursor.execute(
            "SELECT publisher_id FROM Publishers WHERE publisher_name = ?",
            (publisher_name,),
        )
        publisher_rows = cursor.fetchall()

        if not publisher_rows:
            print(
                f"Magazine {magazine_title} can't be added. Publisher {publisher_name} is not in database."
            )
            return

        publisher_id = publisher_rows[0][0]

        cursor.execute(
            "INSERT INTO Magazines (magazine_title, publisher_id) VALUES (?,?)",
            (magazine_title, publisher_id),
        )
    except sqlite3.IntegrityError:
        print(f"{magazine_title} from {publisher_name} already in the database.")


def add_subscriber(cursor, subscriber_name, address):
    cursor.execute(
        "SELECT * FROM Subscribers WHERE subscriber_name = ? AND address = ?",
        (subscriber_name, address),
    )
    results = cursor.fetchall()
    if results:
        print(
            f"Subscriber: {subscriber_name} with address: {address} is already in the database."
        )
        return
    cursor.execute(
        "INSERT INTO Subscribers (subscriber_name, address) VALUES (?,?)",
        (subscriber_name, address),
    )


def subscribe_to_magazine(cursor, subscriber_name, address, magazine_title):
    cursor.execute(
        "SELECT subscribers.subscriber_id "
        "FROM subscribers WHERE subscriber_name = ? AND address = ?",
        (subscriber_name, address),
    )
    subscriber_rows = cursor.fetchall()
    if not subscriber_rows:
        print(
            f"Subscriber {subscriber_name} with address {address} is not in database."
        )
        return
    cursor.execute(
        "SELECT magazines.magazine_id " "FROM magazines WHERE magazine_title = ?",
        (magazine_title,),
    )
    magazine_rows = cursor.fetchall()
    if not magazine_rows:
        print(f"Magazine {magazine_title} is not in database.")
        return
    subscriber_id = subscriber_rows[0][0]
    magazine_id = magazine_rows[0][0]
    cursor.execute(
        "INSERT INTO Subscriptions (subscriber_id, magazine_id) VALUES (?,?)",
        (subscriber_id, magazine_id),
    )


cursor = conn.cursor()

# Add code to the main line of your program to populate each of the 4 tables
# with at least 3 entries. Don't forget the commit!

# Run the program several times.
# View the database to ensure that you are creating the right information,
# without duplication.
add_publisher(cursor, "Forbes")
add_publisher(cursor, "New York Times")
add_publisher(cursor, "Bertelsmann")
add_magazine(cursor, "Forbes 1", "Forbes")
add_magazine(cursor, "Forbes 2", "Forbes")
add_magazine(cursor, "Traveler", "National Geographic Society")
add_magazine(cursor, "New York Times 1", "New York Times")
add_magazine(cursor, "Capital 1", "Bertelsmann")
add_subscriber(cursor, "Alice", "123 Mushroom st. 45")
add_subscriber(cursor, "Alice", "123 Mushroom st. 45")
add_subscriber(cursor, "Bob", "123 Mushroom st. 45")
add_subscriber(cursor, "Alice", "456 Mushroom st. 78")
subscribe_to_magazine(cursor, "Alice", "123 Mushroom st. 45", "Forbes 1")
subscribe_to_magazine(cursor, "Bob", "123 Mushroom st. 45", "Traveler")
subscribe_to_magazine(cursor, "Bob", "456 Mushroom st. 78", "Forbes 2")
subscribe_to_magazine(cursor, "Bob", "123 Mushroom st. 45", "Capital 1")


# Write a query to retrieve all information from the subscribers table.
def retrieve_all_subscribers():
    cursor.execute("SELECT * FROM subscribers")
    subscribers_rows = cursor.fetchall()
    print(subscribers_rows)


retrieve_all_subscribers()


# Write a query to retrieve all magazines sorted by name.
def retrieve_magazines():
    cursor.execute("SELECT magazine_title FROM magazines ORDER BY magazine_title ASC")
    magazines_rows = cursor.fetchall()
    print(magazines_rows)


retrieve_magazines()

# Write a query to find magazines for a particular publisher,
# one of the publishers you created. This requires a JOIN.


def find_magazine_and_publisher(cursor, magazine_title, publisher_name):
    cursor.execute(
        "SELECT * FROM magazines JOIN publishers "
        "ON magazines.publisher_id = publishers.publisher_id WHERE magazines.magazine_title = ? AND publishers.publisher_name = ?",
        (magazine_title, publisher_name),
    )
    full_magazine_info = cursor.fetchall()
    if not full_magazine_info:
        print(
            f"Magazine {magazine_title} with publisher {publisher_name} is not in database"
        )
        return
    print(f"Magazine {magazine_title} with publisher {publisher_name} found")


find_magazine_and_publisher(cursor, "Forbes 1", "Forbes")
find_magazine_and_publisher(cursor, "New York Times 1", "Forbes")

conn.commit()
