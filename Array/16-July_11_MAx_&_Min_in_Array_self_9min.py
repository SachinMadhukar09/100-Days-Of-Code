# 11. Maximum and Minimum In Array 
# Basic Accuracy: 77.04% Submissions: 4694 Points: 1
# Given an array arr of size n, find maximum and minimum elements in the array.

# Example 1:

# Input:
# N = 4
# arr[] = {5 4 2 1}
# Output: 5 1
# Example 2:

# Input:
# N = 1
# arr[] = {8}
# Output: 8 8


def maximumElement(arr,n,):
    #return required result
    
    #code here
    # s=0
    # q=arr[0]
    # for i in range(n-1):
    #     if(arr[i]<arr[i+1]):
    #         s=arr[i+1]
    #         if(s>q):
    #             q=s
    # return q
            
    arr.sort()
    return arr[n-1]

def minimumElement(arr,n):
    #return required result
    
    #code here
    # s=0
    # q=arr[0]
    # for i in range(n-1):
    #     if(arr[i]<arr[i+1]):
    #         s=arr[i]
    #         if(s<q):
    #             q=s
    # return s
    
    arr.sort()
    return arr[0]