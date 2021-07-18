arr=[1,2,3,4]
x=3
c=0
arr.sort()
for i in range(len(arr)):
    if(arr[i]<x):
        c+=1
print(c)
        