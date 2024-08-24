class player:
    name = "jpni"
    __salary = 3_000_000

    def get_salary(self):
        return self.__salary

player = player()

print(player.get_salary())
