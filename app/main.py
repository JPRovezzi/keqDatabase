#!/usr/bin/env python3

"""
This is a main file that connects to a SQLite database named `keq.db` with a single table 
`research_data` that includes an `id`, a `data_point` as text, and a `value` as a real number.
"""

import sqlite3
import os

def main():
    sqlconnect()
    pass

def check_database_exists():
    if os.path.exists('keq.db'):
        return True
    else:
        return False
    pass

def sqlconnect():
    # Connect to SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect('keq.db')
    # Create a cursor object using the cursor() method
    cursor = conn.cursor()
    if not check_database_exists():
        # Create table as per requirement
        sql = '''CREATE TABLE research_data(
        id INT PRIMARY KEY NOT NULL,
        name TEXT NOT NULL,
        formula TEXT NOT NULL,
        value_01 REAL NOT NULL,
        temperature_01 REAL NOT NULL,
        value_02 REAL NOT NULL,
        temperature_02 REAL NOT NULL,
        value_03 REAL NOT NULL,
        temperature_03 REAL NOT NULL,
        value_04 REAL NOT NULL,
        temperature_04 REAL NOT NULL,
        value_05 REAL NOT NULL,
        temperature_05 REAL NOT NULL
        )'''
        cursor.execute(sql)

    pass

if __name__ == "__main__":
    main()


