# def bubblesort(a):
#     for i in range(len(a)-1,0,-1):
#         for j in range(i):
#             if a[j]>a[j+1]:
#                 a[j],a[j+1]=a[j+1],a[j]
#     return a
# print(bubblesort(a))



def selectionSort(arr,n):
    #code here
    for i in range(n-1):
        min_ind=i
        for j in range(i+1,n):
            if arr[j]<arr[min_ind]:
                min_ind=j
        arr[min_ind],arr[i]=arr[i],arr[min_ind]
    return arr
# arr=[5,3,63,5,9,2,1,0]
arr=[10,5,8,20,2,18]
n=len(arr)
print(selectionSort(arr,n))