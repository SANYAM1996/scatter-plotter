# making graph by libraries and functions
# programm based on https://campus.datacamp.com/courses/data-visualization-with-seaborn/seaborn-introduction?ex=3
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class data_points(object):
    def __init__(self,value1,value2,value3,value4):
        self.value1 = value1
        self.value2 = value2
        self.value3 = value3
        self.value4 = value4
        
    def get_statement(self):
        print('the given data points are ',self.value1,self.value2,self.value3,self.value4)
a = data_points(1,2,3,4)
b = data_points(6,7,8,9)
a.get_statement()
b.get_statement()
# plotting the function points with the help of list.
x = [1,2,3,4]
y = [6,7,8,9]
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('visualization with function points')
sns.regplot(x,y)
plt.show()
