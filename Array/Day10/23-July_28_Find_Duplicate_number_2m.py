# Link https://leetcode.com/problems/find-the-duplicate-number/

# 23-July 07:05AM-07:10AM 5 min Completed by HELP



# def findDuplicate(nums):
#         D={}
#         for i in nums:
#             if i not in D:
#                 D[i]=1
#             else:
#                 return i
# nums=[1,3,4,2,2]
# print(findDuplicate(nums))


# -----------------GFG Code-----------

# def printRepeating(arr, size):
 
#     print("The repeating elements are: ")
 
#     for i in range(0, size):
 
#         if arr[abs(arr[i])] >= 0:
#             arr[abs(arr[i])] = -arr[abs(arr[i])]
#         else:
#             print(abs(arr[i]), end=" ")
 
 
# Driver code
# arr = [1, 2, 3, 1, 3, 6, 6]
# arr_size = len(arr)
 
# printRepeating(arr, arr_size)


# -------------Using Sorting----------

def duplicate(a,n):
    a.sort()
    for i in range(n-1):
        if(a[i]==a[i+1]):
            return (a[i])
a=[1,3,4,2,2]
n=len(a)
print(duplicate(a,n))    
        