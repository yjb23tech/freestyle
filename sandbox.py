from class_player import Player
from class_tile import Tile
from classes_weapon_set import Cutlass, Dagger, Pistol
from data_structures import arr_options_north, arr_options_east, arr_options_south, arr_options_west, arr_options_quit
from functions import set_player_name, set_player_birth_place, set_player_age

bool_game_is_won = False 
bool_game_is_quit = False 

def play():

    #Things I only need to happen once
    user_player = Player(set_player_name(), set_player_birth_place(), set_player_age())
    print(user_player)

    #Game loop
    while ((bool_game_is_won == False) or (bool_game_is_quit == False)):

        user_player.get_weapon_in_hand()
        user_player.set_weapon_in_hand()
        user_player.display_player_status()

        user_player_input_action = input(f"What next Captain {user_player.str_name}?\n")

        if user_player_input_action in arr_options_north: 
            print("Travelling North")
        elif user_player_input_action in arr_options_east:
            print("Travelling East")
        elif user_player_input_action in arr_options_south:
            print("Travelling South")
        elif user_player_input_action in arr_options_west:
            print("Travelling West")
        elif user_player_input_action in arr_options_quit:
            bool_game_is_quit = True
        else:
            print("On and on")

play()














