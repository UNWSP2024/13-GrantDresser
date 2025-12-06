##
# Program 2.02: CURD_phonebook.py
# Grant Dresser
#   12/05/2025
##

import sqlite3

DB_NAME = 'phonebook.db'

def get_connection():
    """Returns a new connection to the phonebook database."""
    return sqlite3.connect(DB_NAME)

def add_entry():
    """Add a new (Name, Phone) row to Entries."""
    name = input("Enter the person's name: ").strip()
    phone = input("Enter the phone number: ").strip()

    if not name or not phone:
        print("Name and phone number cannot be empty.")
        return

    conn = get_connection()
    cur = conn.cursor()

    try:
        cur.execute("INSERT INTO Entries (Name, Phone) VALUES (?, ?)",
                    (name, phone))
        conn.commit()
        print("Entry added successfully.")
    except sqlite3.OperationalError:
        print("Error: Entries table does not exist. "
              "Run program3_phonebook_setup.py first.")
    except sqlite3.IntegrityError:
        print("An entry with that name already exists.")
    finally:
        conn.close()

def look_up_phone():
    """Look up a person's phone number by name."""
    name = input("Enter the name to look up: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    conn = get_connection()
    cur = conn.cursor()

    try:
        cur.execute("SELECT Phone FROM Entries WHERE Name = ?", (name,))
        row = cur.fetchone()
    except sqlite3.OperationalError:
        print("Error: Entries table does not exist. "
              "Run program3_phonebook_setup.py first.")
        conn.close()
        return

    conn.close()

    if row:
        print(f"{name}'s phone number is: {row[0]}")
    else:
        print("No entry found for that name.")

def change_phone_number():
    """Change the phone number for an existing person."""
    name = input("Enter the name whose phone number you want to change: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    conn = get_connection()
    cur = conn.cursor()

    try:
        cur.execute("SELECT Phone FROM Entries WHERE Name = ?", (name,))
        row = cur.fetchone()
    except sqlite3.OperationalError:
        print("Error: Entries table does not exist. "
              "Run program3_phonebook_setup.py first.")
        conn.close()
        return

    if not row:
        print("No entry found for that name.")
        conn.close()
        return

    print(f"Current phone number for {name}: {row[0]}")
    new_phone = input("Enter the new phone number: ").strip()

    if not new_phone:
        print("New phone number cannot be empty.")
        conn.close()
        return

    cur.execute("UPDATE Entries SET Phone = ? WHERE Name = ?",
                (new_phone, name))
    conn.commit()
    conn.close()
    print("Phone number updated successfully.")

def delete_entry():
    """Delete a row for a specific person by name."""
    name = input("Enter the name of the entry to delete: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    conn = get_connection()
    cur = conn.cursor()

    try:
        cur.execute("SELECT Phone FROM Entries WHERE Name = ?", (name,))
        row = cur.fetchone()
    except sqlite3.OperationalError:
        print("Error: Entries table does not exist. "
              "Run program3_phonebook_setup.py first.")
        conn.close()
        return

    if not row:
        print("No entry found for that name.")
        conn.close()
        return

    print(f"Found entry: {name} - {row[0]}")
    confirm = input("Are you sure you want to delete this entry? (y/n): ").strip().lower()
    if confirm != 'y':
        print("Delete cancelled.")
        conn.close()
        return

    cur.execute("DELETE FROM Entries WHERE Name = ?", (name,))
    conn.commit()
    conn.close()
    print("Entry deleted successfully.")

def list_all_entries():
    """Optional: List all rows in the Entries table."""
    conn = get_connection()
    cur = conn.cursor()

    try:
        cur.execute("SELECT Name, Phone FROM Entries ORDER BY Name")
        rows = cur.fetchall()
    except sqlite3.OperationalError:
        print("Error: Entries table does not exist. "
              "Run program3_phonebook_setup.py first.")
        conn.close()
        return

    conn.close()

    if not rows:
        print("The phone book is empty.")
        return

    print("\nAll Entries:")
    print("-" * 35)
    print(f'{"Name":20}{"Phone":15}')
    print("-" * 35)
    for name, phone in rows:
        print(f'{name:20}{phone:15}')

def main():
    while True:
        print("\nPHONE BOOK MENU")
        print("1. Add new entry")
        print("2. Look up phone number")
        print("3. Change phone number")
        print("4. Delete entry")
        print("5. List all entries (optional)")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == '1':
            add_entry()
        elif choice == '2':
            look_up_phone()
        elif choice == '3':
            change_phone_number()
        elif choice == '4':
            delete_entry()
        elif choice == '5':
            list_all_entries()
        elif choice == '6':
            print("BYE!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

if __name__ == '__main__':
    main()