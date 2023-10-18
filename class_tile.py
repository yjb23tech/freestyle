class Tile: 

    def __init__(self, int_loc_x, int_loc_y, str_name, str_quadrant):

        self.int_loc_x = int_loc_x 
        self.int_loc_y = int_loc_y
        self.str_name = str_name 
        self.str_quadrant = str_quadrant 
    
    def __str__(self):
        
        return (f"Welcome to {self.str_name} Island! This island is in the {self.str_quadrant} quadrant of the map and has coordinates [{self.int_loc_x}, {self.int_loc_y}]")
    
