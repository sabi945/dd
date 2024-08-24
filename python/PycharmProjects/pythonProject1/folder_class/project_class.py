class Player:
    def __init__(self, helath = 100, enrgy = 100):
        self.helath = helath
        self.energy = enrgy
        print("player created")

    def attack(self,monster,damage = 1):
        monster.darah -= damage
        self.energy -= damage
        print("attack")

class Monster:
    def __init__(self, darah = 100):
        self.darah = darah
        print("monster created")



palyer = Player()
moonster = Monster(darah=500)
palyer.attack(moonster, damage=90)
print(moonster.__dict__)

