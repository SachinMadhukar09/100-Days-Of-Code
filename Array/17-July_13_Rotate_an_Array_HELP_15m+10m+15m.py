# Link https://practice.geeksforgeeks.org/problems/rotate-array-by-n-elements-1587115621/1/?track=DS-Python-Arrays&batchId=273

# 16-July 11:05AM-11:20AM 15min Not Completed on Online Compiler
# 19-July 07:25AM-07:35AM 10min Not Completed on Online Compiler
# 19-July 07:43AM-07:58AM 15min Completed By Help Of Ashish



# 13. Rotate Array 
# Easy Accuracy: 50.28% Submissions: 66568 Points: 2
# Given an unsorted array arr[] of size N, rotate it by D elements in the counter-clockwise direction. 

 

# Example 1:

# Input:
# N = 5, D = 2
# arr[] = {1,2,3,4,5}
# Output: 3 4 5 1 2
# Explanation: 1 2 3 4 5  when rotated
# by 2 elements, it becomes 3 4 5 1 2.
# Example 2:

# Input:
# N = 10, D = 3
# arr[] = {2,4,6,8,10,12,14,16,18,20}
# Output: 8 10 12 14 16 18 20 2 4 6
# Explanation: 2 4 6 8 10 12 14 16 18 20 
# when rotated by 3 elements, it becomes 
# 8 10 12 14 16 18 20 2 4 6.


# a=[1,2,3,4,5]
# # rotate by d
# d=2
# n=len(a)
# b=a[d:]+a[:d]
# print(b)
# print(a[2:5]+a[0:2])
# print(a[d:]+a[:d])
# expected ooutput=[3,4,5,1,2]



# n = 10 
# d = 3
# a= [2,4,6,8,10,12,14,16,18,20]
# t=[]
# # n=len(a)
# for i in range(0,d):
#     t.append(a[i])
# print(t)
# for i in range(d):
#     a.remove(a[i])
# for i in range(n-1,0,-1):
#     a[i]=a[i-1]
# for i in range(len(t)):
#     a.append(t[i])
# print(a)



# ----------------Ashish Code-------------

# def rotateArr(A,D,N):
#         #Your code here
#         temp=A[:D]
#         for i in range(N-D):
#             A[i]=A[D+i]
#         for i in range(N-1,N-D-1,-1):
#             D-=1
#             A[i]=temp[D]
#         return A

# N = 10 
# D = 3
# A= [2,4,6,8,10,12,14,16,18,20]
# print(rotateArr(A,D,N))
 
 
# ----------------Prashant Code-------------

def rotateARr(A,D,N):
    index=0
    temp=A[:D]
    for i in range(N-D):
        A[index]=A[D+index]
        index+-1
    for j in temp:
        A[index]=j
        index+=1
    return A
        

N = 10 
D = 3
A= [2,4,6,8,10,12,14,16,18,20]
print(rotateARr(A,D,N))
 