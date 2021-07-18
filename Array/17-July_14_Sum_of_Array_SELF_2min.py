#16-July 11:20AM-11:22AM Completed SELF

# 14. Sum of Array Elements 
# Easy Accuracy: 61.02% Submissions: 30743 Points: 2
# Given an integer array arr of size n, you need to sum the elements of arr.

# Example 1:

# Input:
# n = 3
# arr[] = {3 2 1}
# Output: 6
# Example 2:

# Input:
# n = 4
# arr[] = {1 2 3 4}
# Output: 10



arr= [1, 2, 3, 4]
n=len(arr)
s=0
for i in range(n):
    s=s+i
print(s)