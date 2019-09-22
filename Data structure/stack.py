class stack():
    def __init__(self):
        self.items = []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[-1]

    def get_stacks(self):
        return self.items

s = stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
print(s.get_stacks())
s.pop()
print(s.get_stacks())
s.peek()
print (s.get_stacks())
print(s.peek())
# converting integer into binary by stack data structure


class Stack:

    def __init__(self):
        self.stack=[]
    def push(self,data):
        return self.stack.append(data)
    def pop(self):
        return self.stack.pop()
    def top(self):
        return self.stack[-1]
    def emp(self):
        if self.stack==[]:
            return True
        else:
            return False
        def get(self):

            return self.stack
def convert(stack,num):
    while num>0:
        c=num
        bina=c%2
        stack.push(bina)
        num//=2
    return stack.get()
stack=Stack()
print(convert(stack,27))