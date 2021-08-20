# Creating a list 
# Insert at beginning 
# Insert Values in form of Array
# Calculate Lenght of Array
# Insert Data at index
# Remove Data from index
# Print the list

class Node:
    def __init__(self,data,next):
        self.data=data
        self.next=next

class Linked_List:
    def __init__(self):
        self.head = None

    def insert_at_beg(self,data):
        node=Node(data,next)
        self.head=node
    
    def insert_values(self,data_list):
        self.head=None
        for data in data_list:
            self.insert_at_beg(data)
        
    def get_length(self):
        c=0
        itr=self.head
        while itr:
            c+=1
            itr=itr.next
        return c
    
    def insert_at_index(self,index,data):
        if index<0 or index>self.get_length():
            print("Exception")
        if index==0:
            self.insert_at_beg(data)
        count=0
        itr=self.head
        while itr: 
            if count==index-1:
                node=Node(data,itr.next)
                itr.next=node
            itr=itr.next
            count+=1
            
    def remove_at_index(self,index,data):
        if index<0 or index>self.get_length():
            print("Exception")
        if index==0:
            self.head=self.head.next
        count=0
        itr=self.head
        while itr: 
            if count==index-1:
                itr.next=itr.next.next
                break
            itr=itr.next
            count+=1
    
    def print(self):
        if self.head is None:
            print("Linked List is empty")
            return
        itr=self.head
        llstr=''
        while itr is not None:
            llstr+=str(itr.data)+'-->'
            itr=itr.next
        print(llstr)

ll=Linked_List()
ll.insert_at_beg(8)
ll.insert_at_beg(28)
ll.insert_at_beg(18)
print(ll)