# 07:30AM-07:45AM 15min Not Completed 
# Link - https://practice.geeksforgeeks.org/problems/maximum-product-subarray3604/1#

# Maximum Product Subarray 
# Medium Accuracy: 29.84% Submissions: 60455 Points: 4
# Given an array Arr that contains N integers (may be positive, negative or zero). Find the product of the maximum product subarray.

# Example 1:

# Input:
# N = 5
# Arr[] = {6, -3, -10, 0, 2}
# Output: 180
# Explanation: Subarray with maximum product
# is 6, -3, -10 which gives product as 180.
# Example 2:

# Input:
# N = 6
# Arr[] = {2, 3, 4, 5, -1, 0}
# Output: 120
# Explanation: Subarray with maximum product
# is 2, 3, 4, 5 which gives product as 120.


	# def maxProduct(self,arr, n):
	# 	# code here
	# 	s=arr[0]
	# 	for i in range(n):
	# 	    for j in range(n):
	# 	        q=arr[i]*arr[j]
	# 	        if(q>s):
	# 	            s=q
	# 	return s