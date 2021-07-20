# Link https://leetcode.com/problems/find-the-duplicate-number/

# 20-July 06:30AM-06:45AM 15 min Not Completed

# 287. Find the Duplicate Number
# Medium

# 8372

# 882

# Add to List

# Share
# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

# There is only one repeated number in nums, return this repeated number.

# You must solve the problem without modifying the array nums and uses only constant extra space.

 

# Example 1:

# Input: nums = [1,3,4,2,2]
# Output: 2
# Example 2:

# Input: nums = [3,1,3,4,2]
# Output: 3
# Example 3:

# Input: nums = [1,1]
# Output: 1
# Example 4:

# Input: nums = [1,1,2]
# Output: 1

# -----------TLE------------

nums = [1,1,2]
for i in range(len(nums)-1):
            for j in range(i,len(nums)-1):
                if(nums[i]==nums[j+1]):
                    print(nums[i])