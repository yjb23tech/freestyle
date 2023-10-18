import random 

class Weapon:

    def __str__(self):

        return (f"This is the {self.str_name} and it is {self.str_msg}; this weapon has an attacking power of {self.int_atk_pwr} damage units")

class Cutlass(Weapon):

    def __init__(self):

        self.str_name = "Cutlass"
        self.str_msg = "perfect for close quarter combat"

        self.int_atk_pwr = random.randint(50, 60)

class Dagger(Weapon):

    def __init__(self):

        self.str_name = "Dagger"
        self.str_msg = "ideal for stealth missions when you need to sneak up on an enemy quietly"

        self.int_atk_pwr = random.randint(30, 40)

class Pistol(Weapon):

    def __init__(self):

        self.str_name = "Pistol"
        self.str_msg = "the go to weapon in a gunslinging contest or when you have a medium range target to hit"

        self.int_atk_pwr = random.randint(40, 45)


