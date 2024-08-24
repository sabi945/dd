class mobil:
    def toyota(self):
        print("ini adalah mobil amfibi model toyota")

class motor:
    def honda(self):
        print("ini adalah motor amfibi merek honda")
class perahu:
    def china(self):
        print("ini adalah perahu")
class amfibi(mobil, motor, perahu):
    pass


water = amfibi()
water.china()
water.toyota()
water.honda()