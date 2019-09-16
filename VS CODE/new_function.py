class Addition():
    first = 0
    second = 0
    third = 0
    fourth = 0
    answer = 0
    subtract = 0

    # parameterized constructor
    def __init__(self,f,s,t,p):
        self.first = f
        self.second = s
        self.third = t
        self.fourth = p

    def display(self):
        print('first number = ' + str(self.first))
        print('second number = ' + str(self.second))
        print('third number = ' + str(self.third))
        print('fourth number = ' + str(self.fourth))
        print('Addition of four number = ' + str(self.answer))
        print('Subtraction of four number= ' + str(self.subtract))

    def calculate(self):
        self.answer = self.first + self.second + self.third + self.fourth

    def calculate1(self):
        self.subtract = self.first - self.second - self.third - self.fourth

    # creating object now
obj = Addition(100,200,300,400)
obj.calculate()
obj.calculate1()
obj.display()

count = Addition(23,34,56,67)
count.calculate()
count.calculate1()
count.display()