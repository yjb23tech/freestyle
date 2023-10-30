from class_player import Player
from class_tile import Tile
from classes_weapon_set import Cutlass, Dagger, Pistol
from data_structures import arr_world_map, arr_world_map_front_end
from data_structures import arr_options_north, arr_options_east, arr_options_south, arr_options_west, arr_options_quit
from constants import vector_north_int_loc_x, vector_north_int_loc_y, vector_east_int_loc_x, vector_east_int_loc_y, vector_south_int_loc_x, vector_south_int_loc_y, vector_west_int_loc_x, vector_west_int_loc_y
from functions import set_player_name, set_player_birth_place, set_player_age, set_player_weapon_init
from functions import get_active_tile, deny_chosen_direction, display_world_map_front_end

def play():

    bool_game_is_quit = False
    bool_game_is_won = False

    #Things I only need to happen once
    user_player = Player(set_player_name(), set_player_birth_place(), set_player_age())
    print(user_player)
    set_player_weapon_init(user_player)

    #Game loop
    while ((bool_game_is_won == False) and (bool_game_is_quit == False)):

        print("--------------------------------------------------------------------------------------------------\n")

        display_world_map_front_end(arr_world_map_front_end)

        user_player.display_current_tile_location(arr_world_map)
        user_player_input_action = input(f"\nWhat would you like to do next Captain {user_player.str_name}?\n")

        if user_player_input_action in arr_options_north: 

            active_tile = get_active_tile(vector_north_int_loc_x, vector_north_int_loc_y, user_player, arr_world_map)

            if active_tile == None:
                deny_chosen_direction(arr_world_map, user_player, "North")
            else:
                active_tile.pvp_battle_sequence(user_player)
            
        elif user_player_input_action in arr_options_east:

            active_tile = get_active_tile(vector_east_int_loc_x, vector_east_int_loc_y, user_player, arr_world_map)

            if active_tile == None:
                deny_chosen_direction(arr_world_map, user_player, "East")
            else:
                active_tile.pvp_battle_sequence(user_player)

        elif user_player_input_action in arr_options_south:

            active_tile = get_active_tile(vector_south_int_loc_x, vector_south_int_loc_y, user_player, arr_world_map)

            if active_tile == None:
                deny_chosen_direction(arr_world_map, user_player, "South")
            else:
                active_tile.pvp_battle_sequence(user_player)

        elif user_player_input_action in arr_options_west:

            active_tile = get_active_tile(vector_west_int_loc_x, vector_west_int_loc_y, user_player, arr_world_map)

            if active_tile == None:
                deny_chosen_direction(arr_world_map, user_player, "West")
            else:
                active_tile.pvp_battle_sequence(user_player) 
           
        elif user_player_input_action in arr_options_quit:
            bool_game_is_quit = True
        else:
            print("On and on")

play()














