from data_structures import arr_weapons_inventory 

class Player:

    def __init__(self, str_name, str_birth_place, int_age):

        self.str_name = str_name 
        self.str_birth_place = str_birth_place
        self.int_age = int_age
        self.int_hp = 100 

        self.int_loc_x = 1 
        self.int_loc_y = 1

        self.arr_weapons_inventory = arr_weapons_inventory 
        self.obj_weapon_in_hand = None 
        self.bool_desire_to_change_weapon = False 

    def __str__(self):

        return (f"\nWelcome Captain {self.str_name} from {self.str_birth_place}; {self.int_age} years young and ready to take on the high seas XD")
    
    def get_int_loc_x(self) -> int:
        return self.int_loc_x
    
    def get_int_loc_y(self) -> int:
        return self.int_loc_y 
    
    def display_current_tile_location(self, arr_game_grid):

        current_tile = arr_game_grid[self.get_int_loc_x()][self.get_int_loc_y()]
        print(f"You're currently on {current_tile.str_name} Island with coordinates [{current_tile.int_loc_x}, {current_tile.int_loc_y}] in the {current_tile.str_quadrant} of the map ")
    
    def set_int_loc_x_y(self, mock_int_loc_x, mock_int_loc_y):

        self.int_loc_x = mock_int_loc_x
        self.int_loc_y = mock_int_loc_y


    def display_player_status(self):
        
        print(f"***Current Player Status***\n\nName: {self.str_name}\nHealth Points: {self.int_hp}\nWeapon in Hand: {self.obj_weapon_in_hand.str_name}\n")
    
    def display_weapons_inventory(self):

        print(f"Captain {self.str_name}! You have the following weapons in your arsenal:\n")
        for x, weapon in enumerate(self.arr_weapons_inventory, 1):
            print(f"{x}. {weapon}")
    
    def get_weapon_in_hand(self):

        if self.obj_weapon_in_hand == None:

            print(f"\nCaptain {self.str_name}! You're currently unarmed - is this safe?")
        else:

            print(f"\nCaptain {self.str_name} has the {self.obj_weapon_in_hand.str_name}")
    
    def set_weapon_in_hand(self):

        if self.obj_weapon_in_hand == None:

            self.equip_weapon_in_hand()

        else:

            user_input_desire_to_change_weapon = input("Would you like to change your weapon?\n")

            if user_input_desire_to_change_weapon in ['Yes', 'YES', 'yes', 'Y', 'y']:
                self.bool_desire_to_change_weapon = True 
                self.equip_weapon_in_hand()
            else:
                print("No weapon change was made\n")   
    
    def equip_weapon_in_hand(self):

        print(f"\nThese are the weapons in your inventory Captain {self.str_name}:\n")
        x = 1 
        for weapon in self.arr_weapons_inventory:
            print(f"{x}. Weapon Name: {weapon.str_name} Attack Power: {weapon.int_atk_pwr}")
            x += 1 
        
        while ((self.obj_weapon_in_hand == None) or (self.bool_desire_to_change_weapon == True)):

            user_input_weapon_in_hand = int(input(f"\nPick from the weapons above; enter the number corresponding to your weapon of choice:\n"))

            if user_input_weapon_in_hand == 1:
                self.obj_weapon_in_hand = self.arr_weapons_inventory[user_input_weapon_in_hand - 1]
                print(f"\nYour're now wielding the {self.obj_weapon_in_hand.str_name}\n")
                self.bool_desire_to_change_weapon = False
            elif user_input_weapon_in_hand == 2:
                self.obj_weapon_in_hand = self.arr_weapons_inventory[user_input_weapon_in_hand - 1]
                print(f"You're now wielding the {self.obj_weapon_in_hand.str_name}\n")
                self.bool_desire_to_change_weapon = False
            elif user_input_weapon_in_hand == 3:
                self.obj_weapon_in_hand = self.arr_weapons_inventory[user_input_weapon_in_hand - 1]
                print(f"You're now wielding the {self.obj_weapon_in_hand.str_name}\n")
                self.bool_desire_to_change_weapon = False
            else:
                print("Bleep Bloop")
            
        

        

        


        

    

    

