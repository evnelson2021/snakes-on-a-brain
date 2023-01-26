#  This module will import sqlite3, and all models for owner, snake and species
# This module will show the initial structure of a SNAKES dictionary
# This module will hold the functions created to get_all_snakes, get_single_snakes, get_snakes_by_species, and create_snake

import sqlite3
from models import Snake, Species

def get_all_snakes():
    # connection to the database
    with sqlite3.connect("./snakes.sqlite3") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # SQL query to get the information you want
        db_cursor.execute("""
        SELECT 
            a.id,
            a.name,
            a.owner_id,
            a.species_id,
            a.gender,
            a.color
        FROM Snakes a
        """)

        # Initialize an empty list to hold all snakes representations
        snakes = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        # for row in dataset:

        for row in dataset:

            # Create an snakes instance from the current row
            snake = Snake(row['id'], row['name'], row['owner_id'], row['species_id'], row['gender'], row['color'])

            # # Add the dictionary representation of the snakes to the list
            snakes.append(snake.__dict__)

    return snakes


def get_single_snake(id):
    with sqlite3.connect("./snakes.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
            SELECT 
                a.id,
                a.name,
                a.owner_id,
                a.species_id,
                a.gender,
                a.color,
                b.id species_id,
                b.name species_name
            FROM Snakes a
            JOIN Species b ON a.species_id = b.id
            WHERE a.id = ?
            """, ( id, ))

            # Load the single result into memory
        data = db_cursor.fetchone()

        if data is None:
            return "Invalid request"

        else:
            # Create an snake instance from the current row
            snake = Snake(data['id'], data['name'], data['owner_id'], data['species_id'], data['gender'], data['color'])

            species = Species(data['species_id'], data['species_name'])

            snake.species = species.__dict__

            # snakes.append(snake.__dict__)

            if species.name == 'Aonyx cinerea':
                return ""

            else:
                return snake.__dict__

# (data, id) = self.parse_url(self.path)

def create_snake(new_snake):
    with sqlite3.connect("./snakes.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Snakes
            ( name, owner_id, species_id, gender, color )
        VALUES
            ( ?, ?, ?, ?, ? );
        """, (new_snake['name'], new_snake['owner_id'], new_snake['species_id'], new_snake['gender'], new_snake['color'], ))

        # The `lastrowid` property on the cursor will return
        # the primary key of the last thing that got added to
        # the database.
        id = db_cursor.lastrowid

        # Add the `id` property to the snake dictionary that
        # was sent by the client so that the client sees the
        # primary key in the response.
        new_snake['id'] = id


    return new_snake

