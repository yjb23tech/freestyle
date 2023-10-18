from class_player import Player
from classes_weapon_set import Cutlass, Dagger 
from functions import set_player_name, set_player_birth_place, set_player_age

user_player = Player(set_player_name(), set_player_birth_place(), set_player_age())
print(user_player)

test_weapon_1 = Cutlass()
print(test_weapon_1)

test_weapon_2 = Dagger()
print(test_weapon_2)








