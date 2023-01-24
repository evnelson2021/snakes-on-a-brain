# This module will hold the class 'Owner' and define the properties of the Owner object

class Owner():
    """Class that defines the properties for a owner object"""

    # Write the __init__ method here
    def __init__(self, id, first_name, last_name, email):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email