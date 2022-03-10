class House:
    def __init__(self):
        self.__hno = "17A"
        self.__street = "carstreet"
        self.__district = "Salem"
    def printHouse(self):
        print(self.__hno,self.__street,self.__district)

a = House()
a.printHouse()
