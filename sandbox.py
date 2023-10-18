from class_player import Player
from class_tile import Tile
from classes_weapon_set import Cutlass, Dagger, Pistol
from data_structures import arr_world_map
from data_structures import arr_options_north, arr_options_east, arr_options_south, arr_options_west, arr_options_quit
from functions import set_player_name, set_player_birth_place, set_player_age
from functions import get_active_tile

def play():

    bool_game_is_quit = False
    bool_game_is_won = False

    #Things I only need to happen once
    user_player = Player(set_player_name(), set_player_birth_place(), set_player_age())
    print(user_player)

    #Game loop
    while ((bool_game_is_won == False) and (bool_game_is_quit == False)):

        user_player.get_weapon_in_hand()
        user_player.set_weapon_in_hand()
        user_player.display_player_status()

        print(f"x. {user_player.int_loc_x} and y. {user_player.int_loc_y}")

        print(f"You're currently on {arr_world_map[user_player.int_loc_x][user_player.int_loc_y].str_name} Island")
        user_player_input_action = input(f"\nWhat next Captain {user_player.str_name}?\n")

        if user_player_input_action in arr_options_north: 

            vector_north_int_loc_x = 0
            vector_north_int_loc_y = 1
            active_tile = get_active_tile(vector_north_int_loc_x, vector_north_int_loc_y, user_player, arr_world_map)

            if active_tile == None:
                print("NFA")
            else:
                print(f"You're now on {active_tile.str_name} - going North was a good decision Sailor")
                print(f"{active_tile.str_name} has an x loc of {active_tile.int_loc_x} and a y loc of {active_tile.int_loc_y}")

                user_player.int_loc_x = active_tile.int_loc_x 
                user_player.int_loc_y = active_tile.int_loc_y

                print(f"Your new x loc. is {user_player.int_loc_x} and your new y loc. is {user_player.int_loc_y}")
            
        elif user_player_input_action in arr_options_east:

            vector_east_int_loc_x = 1
            vector_east_int_loc_y = 0
            active_tile = get_active_tile(vector_east_int_loc_x, vector_east_int_loc_y, user_player, arr_world_map)


            if active_tile == None:
                print("NFA")
            else:
                print(f"You're now on {active_tile.str_name} - happy sailing East sailor")
                user_player.int_loc_x = active_tile.int_loc_x
                user_player.int_loc_y = active_tile.int_loc_y

        elif user_player_input_action in arr_options_south:

            vector_south_int_loc_x = 0
            vector_south_int_loc_y = -1 
            active_tile = get_active_tile(vector_south_int_loc_x, vector_south_int_loc_y, user_player, arr_world_map)

            if active_tile == None:
                print("NFA")
            else:
                print(f"You're now on {active_tile.str_name} - happy sailing South sailor")
                user_player.int_loc_x = active_tile.int_loc_x
                user_player.int_loc_y = active_tile.int_loc_y 

        elif user_player_input_action in arr_options_west:

            vector_west_int_loc_x = -1 
            vector_west_int_loc_y = 0
            active_tile = get_active_tile(vector_west_int_loc_x, vector_west_int_loc_y, user_player, arr_world_map)

            if active_tile == None:
                print("NFA")
            else:
                print(f"You're now on {active_tile.str_name} - happy sailing West sailor")
                user_player.int_loc_x = active_tile.int_loc_x 
                user_player.int_loc_y = active_tile.int_loc_y 
           
        elif user_player_input_action in arr_options_quit:
            bool_game_is_quit = True
        else:
            print("On and on")

play()














