class stack:
    def __init__(self):
        self.items=[]
        
    def push(self,data):
        self.items.append(data)
        
    def pop(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)
    def peek(self):
        return self.items
S=stack()
S.push(10)
S.push(20)
S.push(30)
S.push(40)
print(S.items)
print(S.pop())
# print(S.items)
print(S.peek())
print(S.size())