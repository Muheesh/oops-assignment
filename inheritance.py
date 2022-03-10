class Father(object):
    def __init__(self,fname,fage,foccupation):
        self.fname = fname
        self.fage = fage
        self.foccupation = foccupation
    def printFather(self):
        print("Father name",self.fname)
        print("Father age",self.fage)
        print("Father occupation",self.foccupation)
class Mother(object):
    def __init__(self,mname,mage,moccupation):
        self.mname = mname
        self.mage = mage
        self.moccupation = moccupation
    def printMother(self):
        print("Mother name",self.mname)
        print("Mother age",self.mage)
        print("Mother occupation",self.moccupation)
class child(Father,Mother):
    def __init__(self,name,age,standard):
        self.name = name
        self.age = age
        self.standard = standard
    def printChild(self):
        print("Child Name",self.name)
        print("Child age",self.age)
        print("Child standard",self.standard)

a=Father("Selvam","50","Bussiness")
b=Mother("Thilagavathhy","42","Homemaker")
c=child("Muheesh","20","final year")
while True:
    print("1.Show father details")
    print("2.Show mother details")
    print("3.Show child details")
    a = int(input("Enter the choice"))

    if a==1:
        a.printFather()
    elif a==2:
        b.printMother()
    elif a==3:
        c.printChild()
    else:
        break