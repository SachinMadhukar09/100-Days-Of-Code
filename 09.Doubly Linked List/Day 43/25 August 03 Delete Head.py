class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

def insertAtBeg(head,data):
    temp=Node(data)
    if head!=None:
        head.prev=temp
    temp.next=head
    return temp

def delHead(head):
    if head==None:
        return None
    if head.next==None:
        return None
    else:
        head=head.next
        head.prev=None
        return head

def delLastNode(head):
    if head==None:
        return None
    if head.next==None:
        return None
    else:
        curr=head
        while curr.next.next!=None:
            curr=curr.next
        curr.next=None
        return head
    
def printList(head):
    curr=head
    while curr!=None:
        print(curr.data,end=" ")
        curr=curr.next
        
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
        curr=curr.next
    return prev

head=Node(20)
head=insertAtBeg(head,30)
head=insertAtBeg(head,40)
head=insertAtBeg(head,50)
printList(head)
print()
head=delHead(head)
printList(head)
head=delLastNode(head)
print()
printList(head)
head=reverseDLL(head)
printList(head)




    