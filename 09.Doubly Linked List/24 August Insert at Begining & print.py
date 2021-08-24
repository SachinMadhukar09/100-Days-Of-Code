class Node:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None

def insertAtBeg(head,x):
    temp=Node(x)
    if head!=None:
        head.prev=temp
    temp.next=head
    # head=temp
    return temp
def printi(head):
    curr=head
    while curr!=None:
        print(curr.data,end="  ")
        curr=curr.next
        
head=Node(5)
head=insertAtBeg(head,10)
head=insertAtBeg(head,20)
head=insertAtBeg(head,30)
printi(head)

