# 7:30AM-7:31AM  1min Revised Self

# Move all negative numbers to beginning and positive to end with constant extra space
# Difficulty Level : Easy
# Last Updated : 09 Jun, 2021
# An array contains both positive and negative numbers in random order. Rearrange the array elements so that all negative numbers appear before all positive numbers.

# Examples : 

# Input: -12, 11, -13, -5, 6, -7, 5, -3, -6
# Output: -12 -13 -5 -7 -3 -6 11 6 5

# ---------------Coding--------------------

a=[-12, 11, -13, -5, 6, -7, 5, -3, -6]
a.sort()
print(a)

# Time Complexity = O(n)
# Auxilary Space = O(1)