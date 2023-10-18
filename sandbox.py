from class_player import Player
from classes_weapon_set import Cutlass, Dagger, Pistol
from functions import set_player_name, set_player_birth_place, set_player_age

user_player = Player(set_player_name(), set_player_birth_place(), set_player_age())
print(user_player)

user_player.display_weapons_inventory()

user_player.get_weapon_in_hand()










