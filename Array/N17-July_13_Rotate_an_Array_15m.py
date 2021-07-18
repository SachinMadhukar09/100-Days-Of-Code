# 16-July 11:05AM-11:20AM 15min Not Copleted on Online Compiler


# 13. Rotate Array 
# Easy Accuracy: 50.28% Submissions: 66568 Points: 2
# Given an unsorted array arr[] of size N, rotate it by D elements in the counter-clockwise direction. 

 

# Example 1:

# Input:
# N = 5, D = 2
# arr[] = {1,2,3,4,5}
# Output: 3 4 5 1 2
# Explanation: 1 2 3 4 5  when rotated
# by 2 elements, it becomes 3 4 5 1 2.
# Example 2:

# Input:
# N = 10, D = 3
# arr[] = {2,4,6,8,10,12,14,16,18,20}
# Output: 8 10 12 14 16 18 20 2 4 6
# Explanation: 2 4 6 8 10 12 14 16 18 20 
# when rotated by 3 elements, it becomes 
# 8 10 12 14 16 18 20 2 4 6.


a=[1,2,3,4,5]
# rotate by d
d=2
n=len(a)
b=a[d:]+a[:d]
print(b)
# print(a[2:5]+a[0:2])
# print(a[d:]+a[:d])
# expected ooutput=[3,4,5,1,2]