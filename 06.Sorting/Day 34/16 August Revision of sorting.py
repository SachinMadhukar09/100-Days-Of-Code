def mergesort(arr,l,m,r):
    i,j,k=0,0,l
    left=arr[l:m+1]
    right=arr[m+1:r]
    while i<len(left) and j<len(right):
        if arr[i]<arr[j]:
            arr[k]=arr[i]
            k=k+1
            i=i+1
        else:
            arr[k]=arr[j]
            k=k+1
            j=j+1
    while i<len(left):
        arr[k]=arr[i]
        i=i+1
        k=k+1
    while j<len(right):
        arr[k]=arr[j]
        j=j+1
        k=k+1
    return arr
arr=[4,5,25,23,52]
l=0
r=len(arr)-1
m=len(arr)//2
print(mergesort(arr,l,m,r))
            