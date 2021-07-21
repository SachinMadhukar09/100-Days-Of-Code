# Link https://practice.geeksforgeeks.org/problems/minimum-number-of-jumps-1587115620/1

# 20-July 05:55PM-06:25AM 30min Not Completed

# Minimum number of jumps 
# Medium Accuracy: 32.96% Submissions: 100k+ Points: 4
# Given an array of N integers arr[] where each element represents the max number of steps that can be made forward from that element. Find the minimum number of jumps to reach the end of the array (starting from the first element). If an element is 0, then you cannot move through that element.
# Note: Return -1 if you can't reach the end of the array.


# Example 1:

# Input:
# N = 11 
# arr[] = {1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9} 
# Output: 3 
# Explanation: 
# First jump from 1st element to 2nd 
# element with value 3. Now, from here 
# we jump to 5th element with value 9, 
# and from here we will jump to last. 
# Example 2:

# Input :
# N = 6
# arr = {1, 4, 3, 2, 6, 7}
# Output: 2 
# Explanation: 
# First we jump from the 1st to 2nd element 
# and then jump to the last element.



arr=[1,3,4,5,9,4,3,5,8]
# arr=[1,4,3,2,6,7]
j=1
c=0
n=len(arr)
for i in range(0,n,j):
    i=i+j
    if(i==n):
        c-=1
        print(c)
    elif(i>n):
        print(c)
    if(arr[i]!=None):
        j=arr[i]
        c=c+1
        print(j)
# else:
# 	    print(c)
print(c)