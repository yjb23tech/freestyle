#test_weapon_1 = Cutlass()
#print(test_weapon_1)

#test_weapon_2 = Dagger()
#print(test_weapon_2)

#test_weapon_3 = Pistol()
#print(test_weapon_3)

#test_tile = Tile(1, 1, "Romance Dawn", "Centre")
    #print(test_tile)
    #user_player.display_weapons_inventory()

#from data_structures import arr_world_map 

#print(" ")
#for x in range(len(arr_world_map)):
#for y in range(len(arr_world_map)):
#print(arr_world_map[x][y])
#print(" ")

#while ((self.obj_weapon_in_hand == None) or (self.bool_desire_to_change_weapon == True)):
#user_input_weapon_in_hand = int(input(f"\nPick from the weapons above; enter the number corresponding to your weapon of choice:\n"))

#if user_input_weapon_in_hand == 1:
#self.obj_weapon_in_hand = self.arr_weapons_inventory[user_input_weapon_in_hand - 1]
#print(f"\nYou're now wielding the {self.obj_weapon_in_hand.str_name}")
#elif user_input_weapon_in_hand == 2:
#self.obj_weapon_in_hand = self.arr_weapons_inventory[user_input_weapon_in_hand - 1]
#print(f"\nYou're now carrying the {self.obj_weapon_in_hand.str_name}")
#elif user_input_weapon_in_hand == 3:
#self.obj_weapon_in_hand = self.arr_weapons_inventory[user_input_weapon_in_hand - 1]
#print(f"\nGunMan! You're now toting the {self.obj_weapon_in_hand.str_name} - point and shoot!")
#else:
#print("\nInput not understood")

#for x in range(len(arr_world_map_front_end_mod[0])):
#print(f"{arr_world_map_front_end_mod[0][x]}", end="")

#print(" ")

#for y in range(len(arr_world_map_front_end_mod[1])):
#print(f"{arr_world_map_front_end_mod[1][y]}", end="")

#* * * * * * * * * * 
#*     *     *     *
#*     *     *     *
#* * * * * * * * * * 
#*     *     *     *
#*     *     *     *
#* * * * * * * * * *
#*     *     *     * 
#*     *     *     *
#* * * * * * * * * *

#* * * * * * * * * * * * * * * *
#*         *         *         *
#*         *         *         *
#*         *         *         *
#*         *         *         *
#* * * * * * * * * * * * * * * *
#*         *         *         * 
#*         *         *         *
#*         *         *         *
#*         *         *         *
#* * * * * * * * * * * * * * * *  

arr_world_map_front_end = [

    ['*',' *'," *"," *"," *"," *"," *"," *"," *"," *"," *"," *"," *"," *"," *"," *"],
    ['*',' ',' ',' ',' ',' ',' '," *",' ',' ',' ',' ',' ',' '," *", ' ',' ',' ',' ',' ',' '," *"],
    ['*',' ',' ','N','W',' ',' '," *",' ',' ',' N',' ',' ',' ',"*", ' ',' ','N','E',' ',' '," *"],
    ['*',' ',' ',' ',' ',' ',' '," *",' ',' ',' ',' ',' ',' '," *", ' ',' ',' ',' ',' ',' '," *"],
    ['*',' ',' ',' ',' ',' ',' '," *",' ',' ',' ',' ',' ',' '," *", ' ',' ',' ',' ',' ',' '," *"],
    ['*',' *'," *"," *"," *"," *"," *"," *"," *"," *"," *"," *"," *"," *"," *"," *"],
    ['*',' ',' ',' ',' ',' ',' '," *",' ',' ',' ',' ',' ',' '," *", ' ',' ',' ',' ',' ',' '," *"],
    ['*',' ',' ',' W',' ',' ',' ',"*",' ',' ',' C',' ',' ',' ',"*", ' ',' ',' E',' ',' ',' ',"*"],
    ['*',' ',' ',' ',' ',' ',' '," *",' ',' ',' ',' ',' ',' '," *", ' ',' ',' ',' ',' ',' '," *"],
    ['*',' ',' ',' ',' ',' ',' '," *",' ',' ',' ',' ',' ',' '," *", ' ',' ',' ',' ',' ',' '," *"],
    ['*',' *'," *"," *"," *"," *"," *"," *"," *"," *"," *"," *"," *"," *"," *"," *"], 
    ['*',' ',' ',' ',' ',' ',' '," *",' ',' ',' ',' ',' ',' '," *", ' ',' ',' ',' ',' ',' '," *"],
    ['*',' ',' ','S','W',' ',' '," *",' ',' ',' S',' ',' ',' ',"*", ' ',' ','S','E',' ',' '," *"],
    ['*',' ',' ',' ',' ',' ',' '," *",' ',' ',' ',' ',' ',' '," *", ' ',' ',' ',' ',' ',' '," *"],
    ['*',' ',' ',' ',' ',' ',' '," *",' ',' ',' ',' ',' ',' '," *", ' ',' ',' ',' ',' ',' '," *"],
    ['*',' *'," *"," *"," *"," *"," *"," *"," *"," *"," *"," *"," *"," *"," *"," *"]

]

#* * * * * * * * * * 
#*     *     *     *
#*     *     *     *
#* * * * * * * * * * 
#*     *     *     *
#*     *     *     *
#* * * * * * * * * *
#*     *     *     * 
#*     *     *     *
#* * * * * * * * * *

arr_world_map_front_end_mod = [

    ['*',' *',' *',' *',' *',' *',' *',' *',' *',' *'],
    ['*','  ','  ',' *','  ','  ',' *','  ','  ',' *'],
    ['*','  ','  ',' *','  ','  ',' *','  ','  ',' *'], 
    ['*',' *',' *',' *',' *',' *',' *',' *',' *',' *'], 
    ['*','  ','  ',' *','  ','  ',' *','  ','  ',' *'],
    ['*','  ','  ',' *','  ','  ',' *','  ','  ',' *'], 
    ['*',' *',' *',' *',' *',' *',' *',' *',' *',' *'], 
    ['*','  ','  ',' *','  ','  ',' *','  ','  ',' *'], 
    ['*','  ','  ',' *','  ','  ',' *','  ','  ',' *'], 
    ['*',' *',' *',' *',' *',' *',' *',' *',' *',' *'] 

]

print(" ")
for x in range(len(arr_world_map_front_end_mod)):
    for y in range(len(arr_world_map_front_end_mod[x])):
        building_block = arr_world_map_front_end_mod[x][y]
        print(f"{building_block}", end="")
    print("")
print(" ")





