from data_structures import arr_weapons_inventory 

class Player:

    def __init__(self, str_name, str_birth_place, int_age):

        self.str_name = str_name 
        self.str_birth_place = str_birth_place
        self.int_age = int_age

        self.arr_weapons_inventory = arr_weapons_inventory 
        self.obj_weapon_in_hand = None 

    def __str__(self):

        return (f"\nWelcome Captain {self.str_name} from {self.str_birth_place}; {self.int_age} years young and ready to take on the high seas XD\n")
    
    def display_weapons_inventory(self):

        print(f"Captain {self.str_name}! You have the following weapons in your arsenal:\n")
        for x, weapon in enumerate(self.arr_weapons_inventory, 1):
            print(f"{x}. {weapon}")
    
    def get_weapon_in_hand(self):

        if self.obj_weapon_in_hand == None:

            print(f"\nCaptain {self.str_name}! You're currently unarmed - is this safe?\n")
        else:

            print(f"\nCaptain {self.str_name} is locked, loaded and ready to go XD\n")
    
    def set_weapon_in_hand(self):

        print(f"Danger is near... you must arm yourself {self.str_name}! Pick a weapon NOW:\n")
        x = 1 
        for weapon in self.arr_weapons_inventory:
            print(f"{x}. Weapon Name: {weapon.str_name}; Attack Power: {weapon.int_atk_pwr}")
            x += 1 
        
        while (self.obj_weapon_in_hand == None):
            user_input_weapon_in_hand = int(input(f"\nPick from the weapons above; enter the number corresponding to your weapon of choice:\n"))

            if user_input_weapon_in_hand == 1:
                self.obj_weapon_in_hand = self.arr_weapons_inventory[user_input_weapon_in_hand - 1]
                print(f"\nYou're now wielding the {self.obj_weapon_in_hand.str_name}")
            elif user_input_weapon_in_hand == 2:
                self.obj_weapon_in_hand = self.arr_weapons_inventory[user_input_weapon_in_hand - 1]
                print(f"\nYou're now carrying the {self.obj_weapon_in_hand.str_name}")
            elif user_input_weapon_in_hand == 3:
                self.obj_weapon_in_hand = self.arr_weapons_inventory[user_input_weapon_in_hand - 1]
                print(f"\nGunMan! You're now toting the {self.obj_weapon_in_hand.str_name} - point and shoot!")
            else:
                print("\nInput not understood")
        


        

    

    

