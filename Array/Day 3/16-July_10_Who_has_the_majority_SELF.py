# 10. Who has the majority? 
# Basic Accuracy: 49.73% Submissions: 45569 Points: 1
# Given an array arr[] of size N and two elements x and y, use counter variables to find which element appears most in the array, x or y. If both elements have the same frequency, then return the smaller element.
# Note:  We need to return the element, not its count.

 

# Example 1:

# Input:
# N = 11
# arr[] = {1,1,2,2,3,3,4,4,4,4,5}
# x = 4, y = 5
# Output: 4
# Explanation: 
# frequency of 4 is 4.
# frequency of 5 is 1.
 

# Example 2:

# Input:
# N = 8
# arr[] = {1,2,3,4,5,6,7,8}
# x = 1, y = 7
# Output: 1
# Explanation: 
# frequency of 1 is 1.
# frequency of 7 is 1.
# Since 1 < 7, return 1.



class Solution:
    #Function to find element with more appearances between two elements in an array.    
    def majorityWins(arr, n, x, y):
        # code here
        c,s=0,0
        for i in range(n):
            if(arr[i]==x):
                c+=1
            if(arr[i]==y):
                s+=1
        if(c>s):
            return x
        elif(s>c):
            return y
        elif(c==s):
            return (min(x,y))

    arr=[1,1,2,2,3,3,4,4,4,4,5]
    n=len(arr)
    x,y,c,s=4,5,0,0
    print(majorityWins(arr,n,x,y))
    
# -------------------------

# Another Solution


a=[1,1,2,2,3,3,4,4,4,4,5]
x,y,c,s=4,5,0,0
for i in range(len(a)):
    if(a[i]==x):
        c+=1
    if(a[i]==y):
        s+=1
if(c>s):
    print(x)
else:
    print(y)