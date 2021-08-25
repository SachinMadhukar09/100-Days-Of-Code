class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
        
def insertAtEnd(head,x):
    temp=Node(x)
    if head==None:
        return temp
    else:
        curr=head
        while curr.next!=None:
            curr=curr.next
        curr.next=temp
        temp.prev=curr
        return head

def printlist(head):
    curr=head
    while curr!=None:
        print(curr.data,end=" ")
        curr=curr.next


head=Node(40)
head=insertAtEnd(head,20)
head=insertAtEnd(head,30)
head=insertAtEnd(head,90)
printlist(head)
