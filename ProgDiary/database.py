import sqlite3

connection = sqlite3.connect('data.db')
connection.row_factory = sqlite3.Row

def create_table():
    with connection:
        connection.execute('CREATE TABLE if not exists entries(content TEXT, date TEXT);')

def add_entry(entry_content, date_content):
    with connection:
        connection.execute(
            "INSERT into entries VALUES(?, ?);", (entry_content, date_content)
        )


def get_entries():
    with connection:
        cursor = connection.execute("SELECT * FROM entries")
    return cursor
