# 06 August 08:43PM-08:59PM 17min 
                           # GFG 
#                  Logic    12min  
#                  Coding   5min 

def bsearch(l,x):
    low=0
    high=len(l)-1
    while low<=high:
        mid=(low+high)//2
        if l[mid]==x:
            return mid
        elif l[mid]<x:
            low=mid+1
        else:
            high=mid-1
    return -1
l=[10,20,30,40,50,60]
x=10
print(bsearch(l,x))
        
        