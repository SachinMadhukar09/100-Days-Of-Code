#Link https://practice.geeksforgeeks.org/problems/count-pairs-with-given-sum5022/1#

# 21-July 07:20AM-07:45AM 25min Not Completed

# Count pairs with given sum
# Easy Accuracy: 41.59% Submissions: 55265 Points: 2
# Given an array of N integers, and an integer K, find the number of pairs of elements in the array whose sum is equal to K.


# Example 1:

# Input:
# N = 4, K = 6
# arr[] = {1, 5, 7, 1}
# Output: 2
# Explanation:
# arr[0] + arr[1] = 1 + 5 = 6
# and arr[1] + arr[3] = 5 + 1 = 6.

# Example 2:

# Input:
# N = 4, X = 2
# arr[] = {1, 1, 1, 1}
# Output: 6
# Explanation:
# Each 1 will produce sum 2 with any 1.

def getPairsCount(arr, n, k):
    # code here
    c = 0
    for i in range(n-1):
        if(arr[i]+arr[i+1] == k):
            c += 1
        for j in range(i, n-1):
            if(arr[i]+arr[j+1] == k):
                # print(arr[i])
                # print(arr[j])
                c += 1
            break
    return c


arr = [1, 5, 7, 1]
n = len(arr)
k = 6
print(getPairsCount(arr, n, k))


# -------------------Old Code--------------

# a=[1,1,1,1]
# a = [1, 5, 7, 1]
# k = 6
# c = 0

# for i in range(len(a)-1):
#     if(a[i]+a[i+1] == k):
#         c += 1
#         for j in range(i, len(a)-1):
#             if(a[i]+a[j+1] == k):
#                 c += 1
#             break
#         # else:
#         #     print("0")
# print(c)
