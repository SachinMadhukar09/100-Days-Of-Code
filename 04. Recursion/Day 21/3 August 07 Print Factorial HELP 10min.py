# 03 August 06:41PM-06:51AM 10min 
                          # SELF    #GFG    
#                  Logic    3min    1min
#                  Coding   6min    1min


# link - https://practice.geeksforgeeks.org/problems/factorial-using-recursion/1/?track=DS-Python-Recursion&batchId=273#

def fun(n):
    if n==1:
        return 1
    return n*fun(n-1)
n=int(input())
print(fun(n))
