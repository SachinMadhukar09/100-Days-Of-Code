# 07 August 06:38AM-06:54AM 16min 
                           # GFG 
#                  Logic    10min  
#                  Coding   6min 

# Time Complexity  - O(logn)

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
            if mid==0 or l[mid-1]!=l[mid]:
                return mid
            else:
                high=mid-1
    return -1
l=[10,10,30,40]
x=10
print(firstoccurence(l,x))