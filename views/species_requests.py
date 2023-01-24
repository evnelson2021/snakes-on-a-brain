#  This module will import sqlite3, and all models for owner, snake and species
# This module will show the initial structure of a SPECIES dictionary
# This module will hold the functions created to get_all_species and get_single_species 

import sqlite3
from models import Species

def get_all_species():
    # connection to the database
    with sqlite3.connect("./snakes.sqlite3") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # SQL query to get the information you want
        db_cursor.execute("""
        SELECT * FROM Species
        """)

        # Initialize an empty list to hold all species representations
        species = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        # for row in dataset:

        for row in dataset:

            # Create an species instance from the current row
            species = Species(row['id'], row['name'])

            # # Add the dictionary representation of the species to the list
            # species.append(species.__dict__)

    return species