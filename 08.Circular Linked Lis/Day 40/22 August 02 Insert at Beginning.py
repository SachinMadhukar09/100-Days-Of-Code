def insertBeg(head,x):
    temp=head(x)
    if head==None:
        temp.next=temp
        return temp
    curr=head
    while curr.next!=head:
        curr=curr.next
    curr.next=temp
    temp.next=head
    return temp