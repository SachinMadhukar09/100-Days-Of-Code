# 03 August 07:11AM-07:16AM 5min 
                          # SELF    #GFG    
#                  Logic    2min    1min
#                  Coding   0min    2min

# link - https://practice.geeksforgeeks.org/problems/sum-of-digits-of-a-number/1/?track=DS-Python-Recursion&batchId=273

def fun(n):
    if n/10==0:
        return 1
    return (n%10)+fun(n//10)
print(fun(64))
