#Link https://practice.geeksforgeeks.org/problems/merge-two-sorted-arrays5135/1

# 20-July 07:05AM-07:15AM 10min Not Completed

# Merge Without Extra Space 
# Hard Accuracy: 36.41% Submissions: 68074 Points: 8
# Given two sorted arrays arr1[] of size N and arr2[] of size M. Each array is sorted in non-decreasing order. Merge the two arrays into one sorted array in non-decreasing order without using any extra space.


# Example 1:

# Input:
# N = 4, M = 5
# arr1[] = {1, 3, 5, 7}
# arr2[] = {0, 2, 6, 8, 9}
# Output: 0 1 2 3 5 6 7 8 9
# Explanation: Since you can't use any 
# extra space, modify the given arrays
# to form 
# arr1[] = {0, 1, 2, 3}
# arr2[] = {5, 6, 7, 8, 9}

# Example 2:

# Input:
# N = 2, M = 3
# arr1[] = {10, 12}
# arr2[] = {5, 18, 20}
# Output: 5 10 12 18 20
# Explanation: Since you can't use any
# extra space, modify the given arrays
# to form 
# arr1[] = {5, 10}
# arr2[] = {12, 18, 20}

arr1=[1,3,5,7]
n=len(arr1)
arr2=[0,2,6,8,9]
m=len(arr2)
b = []
for i in range(n):
    b.append(arr1[i])
for i in range(m):
    b.append(arr2[i])
b.sort()
print(b)


