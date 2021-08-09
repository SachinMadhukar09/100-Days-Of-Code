# 09 August 06:30AM-06:45AM 15min
                               # GFG
#                  Logic         10min
#                  Coding        5min 

def mergesort(a,b):
    res=[]
    m=len(a)
    n=len(b)
    i=0
    j=0
    while i<m and j<n:
        if a[i]<b[j]:
            res.append(a[i])
            i=i+1
        else:
            res.append(b[j])
            j=j+1
    while i<m:
        res.append(a[i])
        i=i+1
    while j<n:
        res.append(b[j])
        j=j+1
    return res
a=[10,2]
b=[5,6,6,30,40]
print(mergesort(a,b))
            