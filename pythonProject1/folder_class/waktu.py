class kendaraan:
    def __init__(self, ban, unit):
        self.ban = ban
        self.unit = unit
    def about(self):
        return f"ada {self.unit} unit yang per ban {self.ban}"
    
class motor(kendaraan):
    def __init__(self,ban, unit):
        super().__init__(unit, ban)
    def baso(self):
        return f"{super().about()}"

panggilan = motor(1,4)
print(panggilan.baso())