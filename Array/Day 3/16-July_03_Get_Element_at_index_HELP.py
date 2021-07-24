# COmpleted With HELP

# 3. Get Element At Index 
# Basic Accuracy: 75.55% Submissions: 5322 Points: 1
# You are given an array arr(0-based indexing). The size of the array is given by n. You need to get the element at index i and return it. If no element exists at i then return -1.

# Example 1:

# Input:
# n = =6
# arr[] = {1 2 3 4 5 6}
# index = 0
# Output: 1
# Explanation: The array is {1 2 3 4 5 6}.
# The index given is 0. so element at 0th
# index is 1.
# Example 2:

# Input:
# n = 4
# arr[] = {1 2 3 4}
# index = 4
# Output: -1
# Explanation: The array is {1 2 3 4}. The
# index given is 4. Here no element exists
# at the 4th index, so the answer is -1.

# -------------------

# This Code have O(n) Complexity ANd we have to write O(1)

# a=[1,2,3,4]
# k=2
# for i in range(len(a)):
#     if(i==k):
#         print("-1")
        
# -----------------------        

# This Code have O(1) Complexity ANd we have to write O(1)

def getByIndex():
    if idx<=n:
        print(arr[idx])
    else:
        print("-1")

n=3
arr=[1,2,3,4]
idx=2
print(getByIndex())




