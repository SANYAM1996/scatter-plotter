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