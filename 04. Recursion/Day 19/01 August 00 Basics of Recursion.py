# def fun():
#     print("Sachin")
#     fun()
# print(fun())


# Print Your name for n times using Recursion

# 1

# def fun(n):
#     if n<=0:    
#         # --- Base Case
#         return
#     print("Sachin")
#     fun(n-1)
# n=int(input())
# print(fun(n))

# 2

# def fun(n):
#     if n==0:
#         return 
#     print(n)
#     fun(n-1)
#     print(n)
# print(fun(3))

# 3

# def fun(n):
#     if n==0:
#         return 
#     fun(n-1)
#     print(n)
#     fun(n-1)
# print(fun(3))

# 4

# def fun(n):
#     if n<=1:
#         return 0
#     else:
#         return 1+fun(n/2)
# print(fun(16))

# 5

# def fun(n):
#     if n<=1:
#         return 0
#     else:
#         return 1+fun(n/2)
# print(fun(8))

# 6

def fun(n):
    if n<=0:
        return 
    else: 
        fun(n//2)
        print(n%2)
print(fun(7))