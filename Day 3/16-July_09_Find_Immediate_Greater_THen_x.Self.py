
# . Find Immediate Smaller Than X 
# Easy Accuracy: 49.66% Submissions: 22994 Points: 2
# Given an array arr[] of size N containing positive integers and an integer X, find the element in the array which is smaller than X and closest to it.

 

# Example 1:

# Input:
# N = 5
# arr[] = {4 67 13 12 15}
# X = 16
# Output: 67
# Explanation: For a given value 16, there
# are four values which are smaller than
# it. But 15 is the number which is smaller
# and closest to it with minimum difference
# of 1.
 

# Example 2:

# Input:
# N = 5
# arr[] = {1 2 3 4 5}
# X = 1
# Output: 2
# Explanation: No value is smaller than 1.


a= [4 ,67, 13, 12, 15]
x = 16
n=len(a)
b=[]
if(max(a)<x):
    print("-1")
for i in range(n):
    if(a[i]>x):
        b.append(a[i]-x)
print(x+min(b))
         
    

