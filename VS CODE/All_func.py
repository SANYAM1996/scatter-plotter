# making graph by libraries and functions
# programm based on https://campus.datacamp.com/courses/data-visualization-with-seaborn/seaborn-introduction?ex=3
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# class data_points(object):
#     def __init__(self,value1,value2,value3,value4):
#         self.value1 = value1
#         self.value2 = value2
#         self.value3 = value3
#         self.value4 = value4
        
#     def get_statement(self):
#         print('the given data points are ',self.value1,self.value2,self.value3,self.value4)
# a = data_points(1,2,3,4)
# b = data_points(6,7,8,9)
# a.get_statement()
# b.get_statement()
# plotting the function points with the help of list.
# x = [1,2,3,4]
# y = [6,7,8,9]
# plt.xlabel('x axis')
# plt.ylabel('y axis')
# plt.title('visualization with function points')
# sns.regplot(x,y)
# plt.show()


# class Printlist(object):
#     def __init__(self,numberlist):
#         self.numberlist = numberlist

#     def Print_list(self):
#         for item in self.numberlist:
#             print(f"number{item}")
# p = Printlist([1,2,3,4,5,6,7,8,9,10])
# q = Printlist([10,19,18,12,6,5,4,3,2,1])
# p.Print_list()
# q.Print_list()
# p = [1,2,3,4,5,6,7,8,9,10]
# q = [10,19,18,12,6,5,4,3,2,1]
# plt.xlabel('x axis')
# plt.ylabel('y axis')
# plt.title('visualization of points with the help of loop ')
# sns.stripplot(p,q,color='green')
# plt.show()

# trying to read dataframe by making function
# import numpy as np
# import pandas as pd
# class DataShell():
#     # constructor
#     def __init__(self, filename):
#         self.filename = filename # attribute
#     # method
#     def create_datashell(self):
#         self.array = np.genfromtxt(self.filename, delimiter=',', dtype=None)
#         return self.array
# ourDataShell = DataShell('car.csv')
# ourDataShell.create_datashell()

# creating number with the help of inheritence
# class X(object):
#     def __init__(self,a):
#         self.num = a
#     def doubleup(self):
#         self.num *= 2

    # using inheritence property now
# class y(X):
#     def __init__(self,a):
#         X.__init__(self,a)

#     def tripleup(self):
#         self.num *=3
#     def fourtimes(self):
#         self.num *=4
# object = y(4)
# print(object.num)
# object.doubleup()
# print(object.num)
# object.tripleup()
# print(object.num)
# object.fourtimes()
# print(object.num)
# L = [4,8,24,96]
# T = [5,10,15,20]
# plt.plot(L,T,color='red')
# plt.xlabel ('T points')
# plt.ylabel  ('L points')
# plt.title  ('plotting points with the help of inheritence property'.title())
# plt.grid()
# plt.show()
    
# creating function of user defined function with the help of polymorphisim property
# def add(x,y,z,a,b,c,d = 0):
#     return x + y+z
#     return x + y + z+a
#     return x + y + z + a+b
#     return x + y + z + a + b+c
#     return x + y + z + a + b + c+d
# print(add(2,3))
# print(add(4,5,6))
# print(add(2,6,7,4))
# print(add(5,3,1,7,9))
# print(add(9,8,7,6,5,4))
# getting arguments error while running this function


class numbers(): 
    def add(self): 
        print("[2,3,4,5,6,7]") 
  
    def add1(self): 
        print("[3,4,5,6,7,8]") 
  
    def type(self): 
        print("these are the list by first class.".title()) 
  
class numbers2(): 
    def add(self): 
        print("[12,13,14,15,16,17]") 
  
    def add1(self): 
        print("[21,22,23,24,25,26]") 
  
    def type(self): 
        print("this list is from second class.".title()) 
  
obj_num = numbers() 
obj_num2 = numbers2() 
for count in (obj_num, obj_num2): 
    count.add() 
    count.add1() 
    count.type() 
# now plotting graph
x1 = [2,3,4,5,6,7]
y1 = [3,4,5,6,7,8]
p1 = [12,13,14,15,16,17]
q1 = [21,22,23,24,25,26]
plt.plot(x1,y1,p1,q1)
plt.xlabel('axis of x1 and p1')
plt.ylabel('axis of y1 and q1')
plt.legend()
plt.title('points plotted by polymorphisim')
plt.grid()
plt.show()

