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


def kthSmallest(arr, k):
    '''
    arr : given array
    l : starting index of the array i.e 0
    r : ending index of the array i.e size-1
    k : find kth smallest element and return using this function
    '''
    for i in range(k-1):
        arr.remove(min(arr))
    return min(arr)


arr = [1, 4, 7, 2, 45]
k = 4
print(kthSmallest(arr, k))
