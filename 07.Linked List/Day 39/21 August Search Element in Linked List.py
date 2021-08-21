class Node:
    def __init__(self,key):
        self.key=key
        self.next=None
    
def search(head,x):
    pos=1
    curr=head
    while curr!=None:
        if curr.key==x:
            return pos
        pos+=1
        curr=curr.next
head=Node(9)
head.next=Node(10)
head.next.next=Node(15)
head.next.next.next=Node(20)
x=20
print(search(head,x))


class Node:
    def __init__(self,data,next):
        self.data=data
        self.next=next
        
class Linked_List:
    def __init__(self):
        self.head=None
        
    def insert_at_begining(self,data):
        node=Node(data,next)
        self.head=node
        
    def search(self,x):
        pos=1
        itr=self.head
        while itr is None:
            if itr.data==x:
                return pos
            pos+=1
            itr=itr.next
        return -1

ll=Linked_List()
ll.insert_at_begining(10)
ll.insert_at_begining(30)
ll.insert_at_begining(40)
ll.insert_at_begining(20)
print(search(30))


        
                