import sqlite3

DATABASE_PATH = "sqlite.db"  

def create_tables():
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()

    users_table = """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL
    );
    """
    cursor.execute(users_table)

    connection.commit()
    connection.close()

    print("Tables created successfully!")

def insert_data():
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()

    users_table = """
    INSERT INTO users (name, email)
    values ("John Wick", "john.wick@gmail.com")
    """

    cursor.execute(users_table)


    connection.commit()
    connection.close()
    print("Data created successfully!")


create_tables()
insert_data()
