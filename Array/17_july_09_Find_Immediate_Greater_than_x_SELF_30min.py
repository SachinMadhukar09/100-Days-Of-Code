# Completed Self 30min

# 9. Find Immediate Greater Than X 
# Easy Accuracy: 45.62% Submissions: 5776 Points: 2
# Given an array arr[] of size N containing positive integers and an integer X. You need to find the value in the array which is greater than X and closest to it. ( if no such value exists the answer should be -1)

# Example 1:

# Input:
# N = 5
# arr[] = {4 67 13 12 15}
# X = 16
# Output: 67
# Explanation: For a given value 16, there
# is only one value 67 that greater than
# it and so it is the answer.
# Example 2:

# Input:
# N = 5
# arr[] = {1 2 3 4 5}
# X = 1
# Output: 2
# Explanation: For a given value 1, there
# are 4 values greater than it 2 3 4 5.
# But 2 is closest to 1 so it is the answer


arr= [1, 2, 3, 4, 5]
x = 1
# arr= [4 ,67,13, 12, 15]
# x = 16 
n=len(arr)
a=[]
if(max(arr)<x):
    print("-1")
for i in range(n):
    if(arr[i]>x):
        a.append(arr[i]-x)
print(x+min(a))
