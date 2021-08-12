def lomutopartition(a):
    l=0
    h=len(a)-1
    i=l-1
    pivot=a[h]
    for j in range(len(a)):
        if a[j]<pivot:
            i=i+1
            a[i],a[j]=a[j],a[i]
    a[i+1],a[h]=a[h],a[i+1]
    return a
a=[10,80,30,90,50,70]
print(lomutopartition(a))
    