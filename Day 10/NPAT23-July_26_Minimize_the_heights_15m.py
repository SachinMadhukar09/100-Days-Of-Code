# Link https://practice.geeksforgeeks.org/problems/minimize-the-heights3351/1

# 19 july 06:40AM-07:05AM 25min Not Completed
# 23 July 06:25AM-06:40Am 15 min Not completed

# Example 1:

# Input:
# K = 2, N = 4
# Arr[] = {1, 5, 8, 10}
# Output:
# 5
# Explanation:
# The array can be modified as 
# {3, 3, 6, 8}. The difference between 
# the largest and the smallest is 8-3 = 5.
# Example 2:

# Input:
# K = 3, N = 5
# Arr[] = {3, 9, 12, 16, 20}
# Output:
# 11
# Explanation:
# The array can be modified as
# {6, 12, 9, 13, 17}. The difference between 
# the largest and the smallest is 17-6 = 11. 


# -------------------GFG solution---------

def getMinDiff( arr, n, k):
        # code here
        
        arr.sort()
        ans=arr[n-1]-arr[0]
        small,big=0,0
        for i in range(1,n):
            small=min(arr[0]+k,arr[i]-k)
            big=max(arr[i-1]+k,arr[-1]-k)
            ans=min(ans,big-small)
        return ans
k = 3
arr= [2 ,6 ,3 ,4 ,7 ,2 ,10 ,3 ,2 ,1]
n = len(arr)
print(getMinDiff(arr,n,k))
    
    
    
# Not passing All Test Cases
