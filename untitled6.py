import time
start=time.time()
class stack:
    def __init__(self):
        self.items=[]
    def isempty(self):
        return self.items==[]
    def push(self,item):
        self.items.append(item)
        print(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)
S=stack()
print(S.isempty())
print("push operations")
S.push(11)
S.push(12)
S.push(13)
time.sleep(2)
print("the topmost element is:", S.peek())
print("pop operation")
print("the deletion element of stack:", S.pop())
print("the deletion element of stack:", S.pop())
print("the size of stack:", S.size())
end=time.time()
print(f"the runtime program is {end-start}")

        
        
        
        
        
 