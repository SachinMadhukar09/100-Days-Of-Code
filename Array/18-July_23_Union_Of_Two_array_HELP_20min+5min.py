# link https://practice.geeksforgeeks.org/problems/union-of-two-arrays3538/1#

# 18-July 09:10AM-09:20AM 20min Not Completed
# 19-July 08:20AM-08:25AM 5min Completed by Help Prashant



# Union of two arrays 
# Basic Accuracy: 52.81% Submissions: 52701 Points: 1
# Given two arrays a[] and b[] of size n and m respectively. The task is to find union between these two arrays.

# Union of the two arrays can be defined as the set containing distinct elements from both the arrays. If there are repetitions, then only one occurrence of element should be printed in union.

# Example 1:

# Input:
# 5 3
# 1 2 3 4 5
# 1 2 3
# Output: 
# 5
# Explanation: 
# 1, 2, 3, 4 and 5 are the
# elements which comes in the union set
# of both arrays. So count is 5.
# Example 2:

# Input:
# 6 2 
# 85 25 1 32 54 6
# 85 2 
# Output: 
# 7
# Explanation: 
# 85, 25, 1, 32, 54, 6, and
# 2 are the elements which comes in the
# union set of both arrays. So count is 7.


# a=[1,2,3,4,5]
# b=[1,2,3]
# c=[]
# d=[]
# for i in range(len(a)):
#     c.append(a[i])
# for i in range(len(b)):
#     c.append(b[i])
# print(c)
# n=len(c)
# print(n)
# for i in range(n+1):
#     # for j in range(i):
#         if(a[i]==a[i+1]):
#             d.append(a[i])
#         else:
#             d.append(a[i])
# print(d)


# ---------------Prashant Code----------


a=[1,2,3,4,5]
b=[1,2,3]
ans=a+b
print(len(set(ans)))
