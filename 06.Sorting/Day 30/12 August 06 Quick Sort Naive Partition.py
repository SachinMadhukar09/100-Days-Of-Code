# Time Complexity O(n)
# Auxilary Space O(n)


def partition(a,p):
    n=len(a)
    a[p],a[n-1]=a[n-1],a[p]
    temp=[]
    for x in a:
        if x<=a[n-1]:
            temp.append(x)
    for x in a:
        if x>a[n-1]:
            temp.append(x)
    # for i in range(len(a)):
    #     a[i]=temp[i]
    a=temp
    return a
a=[5,13,6,9,12,8,11]
p=5
print(partition(a,p))