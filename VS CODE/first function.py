# sample class with init method
class person():
    # init method or constructor
    def __init__(self,name):
        self.name = name
    # sample method
    def say_hi(self):
        print('Hello my name is ',self.name)
p = person('ron')
p.say_hi()


# make a class for CS student
class CSSstudent():
    # class varaible
    stream = 'cse'
    # the init method
    def __init__(self,roll):
        # instance variable
        self.roll = roll
# object of cssstudent
a = CSSstudent(101)
b = CSSstudent(102)
c = CSSstudent(103)
print(CSSstudent.stream)
print(a.roll)
print(b.stream)
print(b.roll)

# make a class for CS student
class CSSstudent():
    # class varaible
    stream = 'cse'
    # the init method
    def __init__(self,roll):
        # instance variable
        self.roll = roll
    # adds an instance variable
    def setAddress(self,address):
        self.address = address
    # retrive with encapsulation
    def getAddress(self):
        return self.address
a = CSSstudent(101)
a.setAddress('noida up')
print (a.getAddress())