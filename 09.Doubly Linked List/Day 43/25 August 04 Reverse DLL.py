class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

def insertAtBeg(head,data):
    temp=Node(data)
    while head!=None:
        head.prev=temp
    temp.next=head
    return temp

def reverseDLL(head):
    if head==None:
        return None
    if head.next==None:
        return head
    curr=head
    prev=None
    while curr!=None:
        prev=curr
        curr.next,curr.prev=curr.prev,curr.next
        curr=curr.prev
    return prev

def printList(head):
    curr=head
    while curr!=None:
        print(curr.data,end=" ")
        cur=curr.next

head=Node(10)
head=insertAtBeg(head,20)
head=insertAtBeg(head,30)
head=insertAtBeg(head,40)
printList(head)
print()
head=reverseDLL(head)
printList(head)



        