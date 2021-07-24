# Link https://practice.geeksforgeeks.org/problems/inversion-of-array-1587115620/1#

# 21-July 06:25AM-06:40AM  15min TLE

# Count Inversions 
# Medium Accuracy: 39.43% Submissions: 78944 Points: 4
# Given an array of integers. Find the Inversion Count in the array. 

# Inversion Count: For an array, inversion count indicates how far (or close) the array is from being sorted. If array is already sorted then the inversion count is 0. If an array is sorted in the reverse order then the inversion count is the maximum. 
# Formally, two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j.
 

# Example 1:

# Input: N = 5, arr[] = {2, 4, 1, 3, 5}
# Output: 3
# Explanation: The sequence 2, 4, 1, 3, 5 
# has three inversions (2, 1), (4, 1), (4, 3).
# Example 2:

# Input: N = 5
# arr[] = {2, 3, 4, 5, 6}
# Output: 0
# Explanation: As the sequence is already 
# sorted so there is no inversion count.
# Example 3:

# Input: N = 3, arr[] = {10, 10, 10}
# Output: 0
# Explanation: As all the elements of array 
# are same, so there is no inversion count.


# -------------TLE------------------

def inversionCount( arr, n):
        # Your Code Here
        c=0
        for i in range(n):
            for j in range(i,n):
                if(arr[i]>arr[j]):
                    c+=1
        return c
    
arr=[2,4,1,3,5]
n=len(arr)
print(inversionCount(arr,n))
