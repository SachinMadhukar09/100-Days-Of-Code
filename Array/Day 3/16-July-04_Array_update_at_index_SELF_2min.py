# 4. Array Update At Index 
# Easy Accuracy: 87.04% Submissions: 3308 Points: 2
# You are given an array arr(0-based indexing). The size of the array is given by n. You need to update an element at the given index. The arr[i] of the array is initially set to i+1.

# Example 1:

# Input:
# n = 5
# index = 4,element = 8
# Output: 8
# Example 2:

# Input:
# n = 2
# index = 0,element = 99
# Output: 99

def updateArray(a,n,index,element):
    for i in range(n):
        if(i==index):
            a[i]=element
            return a

a=[1,2,3,4]
n=(len(a)-1)
index=2
element=9
print(updateArray(a,n,index,element))