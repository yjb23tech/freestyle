from data_structures import arr_weapons_inventory 

class Player:

    def __init__(self, str_name, str_birth_place, int_age):

        self.str_name = str_name 
        self.str_birth_place = str_birth_place
        self.int_age = int_age

        self.arr_weapons_inventory = arr_weapons_inventory 

    def __str__(self):

        return (f"\nWelcome Captain {self.str_name} from {self.str_birth_place}; {self.int_age} years young and ready to take on the high seas XD\n")
    
    def display_weapons_inventory(self):

        for x, weapon in enumerate(self.arr_weapons_inventory, 1):

            print(f"{x}. {weapon}")
    
    
