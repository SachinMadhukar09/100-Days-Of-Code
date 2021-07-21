# 7:00AM-7:25AM  25min Not Completed 

# Kth smallest element 
# Medium Accuracy: 46.66% Submissions: 87860 Points: 4
# Given an array arr[] and a number K where K is smaller than size of array, the task is to find the Kth smallest element in the given array. It is given that all array elements are distinct.

# Example 1:

# Input:
# N = 6
# arr[] = 7 10 4 3 20 15
# K = 3
# Output : 7
# Explanation :
# 3rd smallest element in the given 
# array is 7.
# Example 2:

# Input:
# N = 5
# arr[] = 7 10 4 20 15
# K = 4
# Output : 15
# Explanation :
# 4th smallest element in the given 
# array is 15.

# ----------------------------------
# -------------Coding---------------

# def kmax(arr,k):
#     s=arr[0]
#     q=[]
#     for i in range(len(arr)-1):
#         if(arr[i]>arr[i+1]):
#             q.append(arr[i+1])
#         else:
#             q.append(arr[i])
#     for i in range(len(q)):
#         s=q[k]
#     return s
# arr=[1,4,7,2,45]
# k=4
# print(kmax(arr,k))



a=[6,3,8,4,1,23]
n=len(a)
q=[]
for i in range(n):
    for j in range(n):
        if(a[i]>a[j]):
            q.append(a[i])
        else:
            # q.append(a[j])  
            break
print(q)        