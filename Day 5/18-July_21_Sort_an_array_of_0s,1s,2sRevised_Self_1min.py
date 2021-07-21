# 7:25AM-7:26AM 1min Revised Self

# Sort an array of 0s, 1s and 2s 
# Easy Accuracy: 51.36% Submissions: 97846 Points: 2
# Given an array of size N containing only 0s, 1s, and 2s; sort the array in ascending order.


# Example 1:

# Input: 
# N = 5
# arr[]= {0 2 1 2 0}
# Output:
# 0 0 1 2 2
# Explanation:
# 0s 1s and 2s are segregated 
# into ascending order.
# Example 2:

# Input: 
# N = 3
# arr[] = {0 1 0}
# Output:
# 0 0 1
# Explanation:
# 0s 1s and 2s are segregated 
# into ascending order.

a=[0,2,1,1,2]
a.sort()
print(a)