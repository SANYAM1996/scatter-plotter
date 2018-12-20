import matplotlib.pyplot as plt
x = [1,3,5,7,9]
y = [2,4,6,8,10]
x1 =[2,4,6,8,10]
y1 =[1,3,5,7,9]
plt.bar(x,y, label = 'first programe', color = 'red')
plt.bar(x1,y1, label = 'second programe', color = 'green') 
plt.title('my bar graph')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.savefig('figure2.png')
plt.legend()
plt.show()
