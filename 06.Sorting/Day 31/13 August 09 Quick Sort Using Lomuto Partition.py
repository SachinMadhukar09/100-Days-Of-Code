def lomutopartition(a,l,h):
    i=l-1
    pivot=a[h]
    for j in range(l,h):
        if a[j]<pivot:
            i=i+1
            a[i],a[j]=a[j],a[i]
    a[i+1],a[h]=a[h],a[i+1]
    return i+1
def qSort(a,l,h):
    if l<h:
        p=lomutopartition(a,l,h)
        qSort(a,l,p-1)
        qSort(a,p+1,h)
    return a
# a=[10,80,30,90,50,70]
a=[8,4,7,9,3,10,5]
l=0
h=len(a)-1
# print(lomutopartition(a,l,h))
print(qSort(a,l,h))
    