# 03 August 06:56PM-07:03AM 9min 
                          # SELF    #GFG    
#                  Logic    3min    0min
#                  Coding   2min    4min

# link - https://practice.geeksforgeeks.org/problems/count-total-digits-in-a-number/1/?track=DS-Python-Recursion&batchId=273


# My Code------
def fun(n):
    if n//10==0:
        return 1
    return 1+fun(n//10)
print(fun(43874))


# Prashant Code-----
def __init__(self):
    self.count=0
def countDigits(self, n):
    if n==0:
        return 1
    else:
        self.count+=1
        self.countDigits(n//10)
        return self.count