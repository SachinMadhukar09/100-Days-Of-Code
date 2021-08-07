# 07 August 07:15AM-07:24AM 9min 
                           # GFG 
#                  Logic    2min  
#                  Coding   7min

# time Complexity - O(logn)

def firstoccurence(l,x):
    low=0
    high=len(l)-1
    while low<=high:
        mid=(low+high)//2
        if l[mid]<x:
            low=mid+1
        elif l[mid]>x:
            high=mid-1
        else:
            if mid==0 or l[mid]!=l[mid-1]:
                return mid
            else:
                high=mid-1
            

def lastoccurence(l,x):
    low=0
    high=len(l)-1
    while low<=high:
        mid=(low+high)//2
        if l[mid]<x:
            low=mid+1
        elif l[mid]>x:
            high=mid-1
        else:
            if mid==0 or l[mid]!=l[mid+1]:
                return mid
            else:
                low=mid+1
def numberofoccurence(l,x):
    first=firstoccurence(l,x)
    if first==-1:
        return 0
    else:
        return lastoccurence(l,x)-first+1
            
l=[10,10,10,20]
x=10
print("First Occurencce")
print(firstoccurence(l,x))
print("Last Occurencce")
print(lastoccurence(l,x))
print("Number of Occurence")
print(numberofoccurence(l,x))
