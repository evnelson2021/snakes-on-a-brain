#  This module will import sqlite3, and all models for owner, snake and species
# This module will show the initial structure of a SNAKES dictionary
# This module will hold the functions created to get_all_snakes, get_single_snakes, get_snakes_by_species, and create_snake

import sqlite3
from models import Snake
from http.server import BaseHTTPRequestHandler, HTTPServer
# from request_handler import _set_headers


def _set_headers(self, status):
    """Sets the status code, Content-Type and Access-Control-Allow-Origin
    headers on the response

    Args:
        status (number): the status code to return to the front end
    """
    self.send_response(status)
    self.send_header('Content-type', 'application/json')
    self.send_header('Access-Control-Allow-Origin', '*')
    self.end_headers()

def do_OPTIONS(self):
    """Sets the options headers
    """
    self.send_response(200)
    self.send_header('Access-Control-Allow-Origin', '*')
    self.send_header('Access-Control-Allow-Methods','GET, POST, PUT, DELETE')
    self.send_header('Access-Control-Allow-Headers','X-Requested-With, Content-Type, Accept')
    self.end_headers()

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
            a.color
        FROM Snakes a
        WHERE a.id = ?
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an snake instance from the current row
        snake = Snake(data['id'], data['name'], data['owner_id'], data['species_id'], data['gender'], data['color'])

        # (data, id) = self.parse_url(self.path)
        if ['species_id'] == '2':
            self._set_headers(405)
        else:
            self._set_headers(200)
            get_single_snake(id)

    return snake.__dict__


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

