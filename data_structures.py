from class_tile import Tile 
from classes_weapon_set import Weapon, Cutlass, Dagger, Pistol

arr_world_map = [

    [Tile(0, 0, "Dressrosa", "South Western"), Tile(0, 1, "Drum", "West"), Tile(0, 2, "Marineford", "North Western")], 
    [Tile(1, 0, "Punk Hazard", "South"), Tile(1, 1, "Romance Dawn", "Central" ), Tile(1, 2, "Elbaf", "North")], 
    [Tile(2, 0, "Fishman", "South Eastern"), Tile(2, 1, "Punk Records", "Eastern" ), Tile(2, 2, "Skypeia", "North Eastern")]

]

arr_weapons_inventory = [Cutlass(), Dagger(), Pistol()]

arr_options_north = ['North', 'NORTH', 'north', 'N', 'n', '^']
arr_options_east = ['East', 'EAST', 'east', 'E', 'e', '>']
arr_options_south = ['South', 'SOUTH', 'south', 'S', 's', 'v']
arr_options_west = ['West', 'WEST', 'west', 'W', 'w', '<']
arr_options_quit = ['Quit', 'QUIT', 'quit', 'Q', 'q', 'q']



