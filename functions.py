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

    print(f"The values to be tested are x: {player_new_int_loc_x} and y: {player_new_int_loc_y}")

    try:

        if ((player_new_int_loc_x < 0) or (player_new_int_loc_y < 0)):
            raise IndexError

        working_tile = arr_game_grid[player_new_int_loc_x][player_new_int_loc_y]
        return working_tile
    
    except IndexError:
            return None