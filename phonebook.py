##
# Program 2.01: phonebook.py
# Grant Dresser
#   12/05/2025
##

import sqlite3

DB_NAME = 'phonebook.db'

def main():
    create_database_and_table()

def create_database_and_table():
    """Creates phonebook.db and the Entries table."""
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    # Create the Entries table if it does not exist.
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Entries (
            Name  TEXT PRIMARY KEY,
            Phone TEXT NOT NULL
        )
    ''')

    conn.commit()
    conn.close()
    print("phonebook.db is ready and the Entries table has been created.")

if __name__ == '__main__':
    main()