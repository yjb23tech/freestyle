def set_player_weapon_init(player):
     
     player.get_weapon_in_hand()
     player.set_weapon_in_hand()
     player.display_player_status()

def set_player_name() -> str:

    user_input_name = input("\nWhat is your name Sailor?\n")
    return user_input_name

def set_player_birth_place() -> str:

    user_input_birth_place = input("\nWhere are you from, Sailor?\n")
    return user_input_birth_place

def set_player_age() -> int:

    user_input_age = int(input("\nAnd how old are you Sailor?\n"))
    return user_input_age

def get_active_tile(x_direction_int_loc_x, y_direction_int_loc_y, player, arr_game_grid):

    player_new_int_loc_x = player.int_loc_x + x_direction_int_loc_x
    player_new_int_loc_y = player.int_loc_y + y_direction_int_loc_y

    try:

        if ((player_new_int_loc_x < 0) or (player_new_int_loc_y < 0)):
            raise IndexError

        working_tile = arr_game_grid[player_new_int_loc_x][player_new_int_loc_y]
        return working_tile
    
    except IndexError:
            return None

def deny_chosen_direction(arr_game_grid, obj_user_player, str_chosen_direction):
    
    current_tile_location = arr_game_grid[obj_user_player.get_int_loc_x()][obj_user_player.get_int_loc_y()]
    print(f"\nAttempting to travel {str_chosen_direction} from {current_tile_location.str_name} will take you to uncharted waters Captain {obj_user_player.str_name}")
    print(f"Your ship will therefore remain docked on {current_tile_location.str_name}")

def display_world_map_front_end(arr_game_grid):
     
     for x in range(len(arr_game_grid)):
        for y in range(len(arr_game_grid[x])):
            building_block = arr_game_grid[x][y]
            print(f"{building_block}", end=" ")
        print("")



