# 19 july 06:40AM-07:05AM 25min Not Completed

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


def getMinDiff(self, arr, n, k):
        # code here
        for i in range(n):
            if arr[i]<10:
                arr[i]=arr[i]+k
            if(arr[i]>=10):
                arr[i]=arr[i]-k
        # return arr
        return (max(arr)-min(arr))