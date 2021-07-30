# 30 July 1:10PM-01:26PM 6min 
                          # SELF    GFG
#                  Logic    3min    5min 
#                  Coding   3min    5min

# 30 July 08:15PM-08:30PM 15min 
                          #  GFG
#                  Logic    10min
#                  Coding   5min

# Link https://practice.geeksforgeeks.org/problems/find-triplets-with-zero-sum/1/?problemType=functional&difficulty[]=-1&difficulty[]=0&page=1&sortBy=submissions&category[]=Hash&query=problemTypefunctionaldifficulty[]-1difficulty[]0page1sortBysubmissionscategory[]Hash#


# Find all triplets with zero sum
# Difficulty Level : Medium
# Last Updated : 12 Jul, 2021
# Given an array of distinct elements. The task is to find triplets in the array whose sum is zero.

# Examples : 

# Input : arr[] = {0, -1, 2, -3, 1}
# Output : (0 -1 1), (2 -3 1)

# Explanation : The triplets with zero sum are
# 0 + -1 + 1 = 0 and 2 + -3 + 1 = 0  

# Input : arr[] = {1, -2, 1, 0, 5}
# Output : 1 -2  1
# Explanation : The triplets with zero sum is
# 1 + -2 + 1 = 0   


# ---My Code----

# arr=[-7,-1,0,3,4]
# arr.sort()
# b=[]
# for i in range(len(arr)):
#     if(arr[i]==0):
#         b.append(arr[i])
#         b.append(arr[i-1])
#         b.append(arr[i+1])
# if sum(b)==0:
#     print("1")
# else:
#     print("0")
    
# ---GFG Code---

def findTriplets(arr, n):
    found = False
    for i in range(0, n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if (arr[i] + arr[j] + arr[k] == 0):
                    # print(arr[i], arr[j], arr[k])
                    found = True
                    # print("1") 
    # If no triplet with 0 sum
    # found in array
    if (found == True):
        print("exist")
    elif(found == False):
        print(" not exist ")
    # else (found == True):
        # print("1")
# Driver code
arr = [87, 0, 100, -3, 71 ,-1, 44]
n = len(arr)
findTriplets(arr, n)