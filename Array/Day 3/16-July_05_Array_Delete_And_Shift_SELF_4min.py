# 5. Array Delete And Shift 
# Easy Accuracy: 65.29% Submissions: 4502 Points: 2
# You are given an array arr(0-based indexing). The size of the array is given by n. You need to delete an element at given index and print the modified array. The arr[i] of array is initially set to i+1.
# Deletion means you need to shift all the elements after that index to the left by 1 position and set the last element as zero.

# Example 1:

# Input:
# n = 5
# index = 0
# Output: 2 3 4 5 0
# Example 2:

# Input:
# n = 6
# index = 3
# Output: 1 2 3 5 6 0

def deleteFromArray(a,n,index):
    for i in range(n):
        if(i==index):
            a.pop(index)
            a.append(0)
            return a
a=[1,2,3,4,5]
n=4
index=0
print(deleteFromArray(a,n,index))