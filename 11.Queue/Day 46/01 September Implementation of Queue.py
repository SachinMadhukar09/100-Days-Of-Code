class Node:
    def __init__(self,k):
        self.key=k
        self.next=None
        
class Myqueue:
    def __init__(self):
        self.front=None
        self.rear=None
        self.size=0
        
    def size(self):
        return self.size
    
    def getFront(self):
        return self.front.key
    
    def getRear(self):
        return self.rear.key
    
    def isEmpty(self):
        return (self.size==0)
    
    def enqueue(self,x):
        temp=Node(x)
        if self.rear==None: 
            self.front=temp
        else:
            self.rear.next=temp
        self.rear=temp
        self.size+=1
        
    def dequeue(self):
        if self.front==None:
            return None
        else:
            res=self.front.key
            self.front=self.front.next
            if self.front==None:
                self.rear=None
            self.size-=1
            return res
        
q=Myqueue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
# q.size()
q.getFront()
q.getRear()
q.isEmpty()
q.dequeue()

        
            