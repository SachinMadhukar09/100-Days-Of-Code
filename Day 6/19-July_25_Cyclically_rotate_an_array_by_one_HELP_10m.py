# 06:25AM-06:35AM  Help  10min

# Cyclically rotate an array by one 
# Basic Accuracy: 64.05% Submissions: 38127 Points: 1
# Given an array, rotate the array by one position in clock-wise direction.
 

# Example 1:

# Input:
# N = 5
# A[] = {1, 2, 3, 4, 5}
# Output:
# 5 1 2 3 4
 

# Example 2:

# Input:
# N = 8
# A[] = {9, 8, 7, 6, 4, 2, 1, 3}
# Output:
# 3 9 8 7 6 4 2 1


def r(a,n):
    t=a[n-1]
    for i in range(n-1,0,-1):
        a[i]=a[i-1]
    a[0]=t
    return a
n = 8
a = [9, 8, 7, 6, 4, 2, 1, 3]
print(r(a,n))
