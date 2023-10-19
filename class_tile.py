class Tile: 

    def __init__(self, int_loc_x, int_loc_y, str_name, str_quadrant):

        self.int_loc_x = int_loc_x 
        self.int_loc_y = int_loc_y
        self.str_name = str_name 
        self.str_quadrant = str_quadrant 
    
    def __str__(self):
        
        return (f"\nWelcome to {self.str_name} Island! This island is in the {self.str_quadrant} quadrant of the map and has coordinates [{self.int_loc_x}, {self.int_loc_y}]")
    
    def pvp_battle_sequence(self, player):

        print(self)
        print(f"Are you ready to do battle {player.str_name}? Gear up!")

        player.get_weapon_in_hand()
        player.set_weapon_in_hand()
        player.display_player_status()

        player.set_int_loc_x_y(self.int_loc_x, self.int_loc_y)


    
