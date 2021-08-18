def merge(arr,left,right):
    i,j,k=0,0,0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            arr[k]=left[i]
            i+=1
        else:
            arr[k]=right[j]
            j+=1
        k+=1
    while i<len(left):
        arr[k]=left[i]
        i+=1
        k+=1
    while j<len(right):
        arr[k]=right[j]
        j+=1
        k+=1    
def mergeSort(arr):
    if len(arr)>1:
        m=len(arr)//2
        left=arr[:m]
        right=arr[m:]
        mergeSort(left)
        mergeSort(right)
        merge(arr,left,right)
arr=[4,8,2,53,12,78,9]
print(mergeSort(arr))
print(arr)