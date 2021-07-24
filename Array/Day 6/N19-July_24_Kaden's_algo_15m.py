# 06:10AM-06:25AM Not Understand the question

# Kadane's Algorithm 
# Medium Accuracy: 51.0% Submissions: 100k+ Points: 4
# Given an array arr of N integers. Find the contiguous sub-array with maximum sum.


# Example 1:

# Input:
# N = 5
# arr[] = {1,2,3,-2,5}
# Output:
# 9
# Explanation:
# Max subarray sum is 9
# of elements (1, 2, 3, -2, 5) which 
# is a contiguous subarray.
# Example 2:

# Input:
# N = 4
# arr[] = {-1,-2,-3,-4}
# Output:
# -1
# Explanation:
# Max subarray sum is -1 
# of element (-1)



def maxSubArraySum(a,size):
        ##Your code here
        max_sum=max(a)
        s=0
        for i in range(size):
            s=s+a[i]
            if(s<0):
                s=0
            elif(max_sum<s):
                max_sum=s
        return max_sum
a = [-1,-2,-3,-4]
size=len(a)
print(maxSubArraySum(a,size))
