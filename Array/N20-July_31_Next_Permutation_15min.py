# link  https://leetcode.com/problems/next-permutation/

# 20-July 07:35Am-07:50AM 15 min Not Completed

# 31. Next Permutation
# Medium

# 6350

# 2107

# Add to List

# Share
# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

# If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).

# The replacement must be in place and use only constant extra memory.

 

# Example 1:

# Input: nums = [1,2,3]
# Output: [1,3,2]
# Example 2:

# Input: nums = [3,2,1]
# Output: [1,2,3]
# Example 3:

# Input: nums = [1,1,5]
# Output: [1,5,1]
# Example 4:

# Input: nums = [1]
# Output: [1]


    #   for i in range(len(nums)-2):
    #         if(nums[i+1]>nums[i]):
    #             nums[i+1],nums[i]=nums[i],nums[i+1]
    #         if(nums[i+1]<nums[i]):
    #             nums[i+1],nums[i]=nums[i],nums[i+1]
    #         if(nums[i+1]==nums[i]):
    #             nums[i+1],nums[i+2]=nums[i+2],nums[i+1]
    #         if(len(nums)==1):
    #             nums=nums