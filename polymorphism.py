class vehicle():
    pass
class suv(vehicle):
    def __init__(self,name,price,topspeed):
        self.name = name
        self.price = price
        self.topspeed = topspeed
    def printvehicle(self):
        print("Suv name",self.name)
        print("suv price",self.price)
        print("suv topspeed",self.topspeed)
class sedan():
    def __init__(self,sname,sprice,stopspeed):
        self.sname = sname
        self.sprice = sprice
        self.stopspeed = stopspeed
    def printvehicle(self):
        print("Sedan name:",self.sname)
        print("Sedan price:",self.sprice)
        print("Sedan Topspped",self.stopspeed)
a = suv("Fortuner","40","200")
b = sedan("Octi","25","260")
a.printvehicle()
b.printvehicle()
