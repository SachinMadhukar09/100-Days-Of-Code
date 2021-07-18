
# . Find Immediate Smaller Than X 
# Easy Accuracy: 49.66% Submissions: 22994 Points: 2
# Given an array arr[] of size N containing positive integers and an integer X, find the element in the array which is smaller than X and closest to it.

 

# Example 1:

# Input:
# N = 5
# arr[] = {4 67 13 12 15}
# X = 16
# Output: 15
# Explanation: For a given value 16, there
# are four values which are smaller than
# it. But 15 is the number which is smaller
# and closest to it with minimum difference
# of 1.
 

# Example 2:

# Input:
# N = 5
# arr[] = {1 2 3 4 5}
# X = 1
# Output: -1
# Explanation: No value is smaller than 1.



# def immediateSmaller(self,arr,n,x):
#     if min(arr)>=x:
#         return -1
#     for i in range(n):
#         if(arr[i]<x):
#             arr[i]=x-arr[i]
#     return x-min(arr)
# arr=[1,2,3,4,5]
# x=1
# n=len(arr)
# print(immediateSmaller(arr,n,x))

# ----------------------
# Clone Of Above Code

# arr=[1,2,3,4,5]
# x=1
a= [4 ,67, 13, 12, 15]
x = 16
n=len(a)
if min(a)>=x:
    print("-1")
for i in range(n):
    if(a[i]<x):
        a[i]=x-a[i]
print(x-min(a))
    



