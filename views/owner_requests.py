#  This module will import sqlite3, and all models for owner, owner and species
# This module will show the initial structure of an OWNERS dictionary
# This module will hold the functions created to get_all_owners and get_single_owners

import sqlite3
from models import Owner

def get_all_owners():
    # connection to the database
    with sqlite3.connect("./snakes.sqlite3") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # SQL query to get the information you want
        db_cursor.execute("""
        SELECT 
            a.id,
            a.first_name,
            a.last_name,
            a.email
        FROM Owners a
        """)

        # Initialize an empty list to hold all owners representations
        owners = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        # for row in dataset:

        for row in dataset:

            # Create an owners instance from the current row
            owner = Owner(row['id'], row['first_name'], row['last_name'], row['email'])

            # # Add the dictionary representation of the owners to the list
            owners.append(owner.__dict__)

    return owners

def get_single_owner(id):
    with sqlite3.connect("./snakes.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT 
            a.id,
            a.first_name,
            a.last_name,
            a.email
        FROM Owners a
        WHERE a.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an owner instance from the current row
        owner = Owner(data['id'], data['first_name'], data['last_name'], data['email'])

    return owner.__dict__