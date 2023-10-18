from class_player import Player
from class_tile import Tile
from classes_weapon_set import Cutlass, Dagger, Pistol
from functions import set_player_name, set_player_birth_place, set_player_age

user_player = Player(set_player_name(), set_player_birth_place(), set_player_age())
print(user_player)

test_tile = Tile(1, 1, "Romance Dawn", "Centre")
print(test_tile)

user_player.display_weapons_inventory()

user_player.get_weapon_in_hand()

user_player.set_weapon_in_hand()

user_player.display_player_status()

user_player.get_weapon_in_hand()
user_player.set_weapon_in_hand()
user_player.display_player_status()













