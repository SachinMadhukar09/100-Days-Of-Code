class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class MyStack:
    def __init__(self):
        self.head=None
        self.size=0
        
    def push(self,x):
        temp=Node(x)
        temp.next=self.head
        self.head=temp
        self.size=self.size+1
    
    def size(self):
        return self.size
    
    def peek(self):
        if self.head==None:
            return ("Error")
        return self.head.data
    
    def pop(self):
        if self.head==None:
            return ("Error")
        res=self.head.data
        self.head=self.head.next
        self.size=self.size-1
        return res
    
s=MyStack()
s.push(10)
s.push(20)
s.push(30)
print(s.pop())
print(s.peek())
print(s.size())