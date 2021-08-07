# 07 August 07:06AM-07:13AM 7min 
                           # GFG 
#                  Logic    4min  
#                  Coding   3min

# Time Complexity  - O(logn)

def lastoccurence(l,x):
    low=0
    high=len(l)-1
    while low<=high:
        mid=(high+low)//2
        if l[mid]>x:
            high=mid-1
        elif l[mid]<x:
            low=mid+1
        else:
            if mid==0 or l[mid]!=l[mid+1]:
                return mid
            else:
                low=mid+1        
    return -1
l=[10,20,20,30,0]
x=20
print(lastoccurence(l,x))