# This module will import all of the functions from each view module to be imported and used in the request_handler.py

from .species_requests import get_all_species, get_single_species
from .snake_requests import get_all_snakes, get_single_snake, create_snake
from .owner_requests import get_all_owners, get_single_owner