def hoarePartiton(a):
    l=0
    h=len(a)-1
    pivot=a[l]
    i=l-1
    j=h+1
    while True:
        i=i+1
        while a[i]<pivot:
            i=i+1
        j=j-1
        while a[j]>pivot:
            j=j-1
        if i>=j:
            return a
        a[i],a[j]=a[j],a[i]
a=[5,3,8,4,2,7,1,10]
print(hoarePartiton(a))