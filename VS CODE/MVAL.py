# using object
class Test():
    def __init__(self):
        self.str = 'molly'
        self.x = 30
def fun():
    return Test()
t = fun()
print(t.str)
print(t.x)

# using tuple
# this gunction returns tuple
def fun():
    str = 'jessica'
    x = 100
    return str,x
str,x = fun()
print(str)
print(x)

# using a list
def fun():
    str = 'theorn'
    x = 40
    return[str,x]
list = fun()
print(list)

# using dictionary
def func():
    d = dict()
    d['name'] = 'rachael'
    d['age'] = '25'
    return d
d = func()
print(d)
