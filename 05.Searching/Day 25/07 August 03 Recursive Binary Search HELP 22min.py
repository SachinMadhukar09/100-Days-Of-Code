# 07 August 06:04AM-06:22PM 18min 
                           # GFG 
#                  Logic    14min  
#                  Coding   4min 


# Time Complexity  - O(logn)
# Space Complexity  - O(logn)

def bsearch(l,x):
    return bSearch(l,x,0,len(l)-1)
def bSearch(l,x,low,high):
    if low>high:
        return -1
    mid=(low+high)//2
    if l[mid]==x:
        return mid
    elif l[mid]>x:
        return bSearch(l,x,low,mid-1)
    elif l[mid]<x:
        return bSearch(l,x,mid+1,high)
l=[10,20,30,40,50]
x=30
print(bsearch(l,x))