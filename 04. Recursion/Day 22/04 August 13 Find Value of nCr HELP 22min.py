# 04 August 06:32AM-06:53AM 22min 
                          # SELF    #GFG    
#                  Logic    2min    1min
#                  Coding   0min    19min

# Link - https://practice.geeksforgeeks.org/problems/find-ncr/1/?track=DS-Python-Recursion&batchId=273

# ------Code From GFG-------
def nCr(n, r):
    return (fact(n) / (fact(r)
                * fact(n - r)))
def fact(n):
    res = 1
    for i in range(2, n+1):
        res = res * i
    return res
n = 5
r = 2
print(int(nCr(n, r)))