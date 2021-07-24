# 7. Count Elements Greater Than X 
# Easy Accuracy: 86.74% Submissions: 3198 Points: 2
# Given an unsorted array arr[] of size N containing non-negative integers. You will also be given an integer X, the task is to count the number of elements which are strictly greater than X. The given integer may or not be present in the array given.

# Example 1:

# Input:
# N = 5
# arr[] = {4 5 3 1 2}
# X = 3
# Output: 2
# Explanation: Here X is 3. The elements
# greater than X are 4 and 5.
# Example 2:

# Input:
# N = 6
# arr[] = {2 2 2 2 2 2}
# X = 3
# Output: 0
# Explanation: Here X is 3. There are no
# elements greater than X.


def greaterThanX(a,n,x):
    c=0
    for i in range(n):
        if(a[i]>x):
            c+=1
    return c


n = 6
a = [2, 2, 2, 2, 2, 2]
x = 3
print(greaterThanX(a,n,x))