# 6. Count Smaller Than X 
# Easy Accuracy: 81.91% Submissions: 3738 Points: 2
# Given an unsorted array arr[] of size N containing non-negative integers. You will also be given an integer X, the task is to count the number of elements which are strictly smaller than X. The given integer may or not be present in the array given.

# Example 1:

# Input:
# N = 5
# arr[] = {4 5 3 1 2}
# X = 3
# Output: 2
# Explanation: Here X = 3, and elements that
# are smaller than X are 1 and 2.
# Example 2:

# Input:
# N = 6
# arr[] = {2 2 2 2 2 2}
# X = 3
# Output: 6
# Explanation: Here X = 3, and elements that
# are smaller than X are 2 2 2 2 2 2.


def smallerThanX(a,n,x):
    c=0
    for i in range(n):
        if(a[i]<x):
            c+=1
    return c
    
a=[2,2,2,2,2,2]
n=6
x=3
print(smallerThanX(a,n,x))