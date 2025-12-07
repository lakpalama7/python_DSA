

class Stack:
    def __init__(self):
        self.stack=[]

    def append(self,value):
        self.stack.append(value)

    def pop(self):
        if self.isEmpty():
            print("Stack is Empty")
        return self.stack.pop()

    def seek(self):
        if self.isEmpty():
            print("Stack is empty")
        return self.stack[-1]

    def isEmpty(self):
        return not bool(self.stack)
    
    def size(self):
        return len(self.stack)
    

s=Stack()
s.append('A')
s.append(1)
s.append('B')
print(s.size())
print(s.pop())
print(s.seek())
print(s.isEmpty())
print(s.stack)