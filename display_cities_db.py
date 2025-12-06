##
# Program 1.02: display_cities_db.py
# Grant Dresser
# 12/05/2025
##


import sqlite3

def main():
    # Connect to the cities database
    conn = sqlite3.connect('cities.db')
    cur = conn.cursor()

    display_cities(cur)

    conn.close()

def display_cities(cur):
    print('Contents of cities.db / Cities table:')
    print('-' * 50)
    cur.execute('SELECT * FROM Cities')
    results = cur.fetchall()

    # HEADER
    print(f'{"ID":<3}{"City":20}{"Population":>15}')
    print('-' * 50)

    for row in results:
        city_id, name, pop = row
        print(f'{city_id:<3}{name:20}{pop:>15,.0f}')

if __name__ == '__main__':
    main()