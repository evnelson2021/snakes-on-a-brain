# This module will hold the class 'Snake' and define the properties of the Snake object

class Snake():
    """Class that defines the properties for a snake object"""

    # Write the __init__ method here
    def __init__(self, id, name, owner_id, species_id, gender, color):
        self.id = id
        self.name = name
        self.owner_id = owner_id
        self.species_id = species_id
        self.gender = gender
        self.color = color