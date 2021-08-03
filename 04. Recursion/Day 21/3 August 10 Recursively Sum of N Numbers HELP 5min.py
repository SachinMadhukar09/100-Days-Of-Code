# 03 August 07:20AM-07:25AM 5min 
                          # SELF    #GFG    
#                  Logic    1min    0min
#                  Coding   2min    2min

# link - https://practice.geeksforgeeks.org/problems/recursively-sum-n-numbers/1/?track=DS-Python-Recursion&batchId=273

def fun(n):
    if n<=1:
        return n
    return n + fun(n-1)

print(fun(5))
