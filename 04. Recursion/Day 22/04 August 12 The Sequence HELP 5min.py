# 03 August 06:25AM-06:29AM 4min 
                          # SELF    #GFG    
#                  Logic    2min    0min
#                  Coding   2min    1min

# Link - https://practice.geeksforgeeks.org/problems/the-sequence/1/?track=DS-Python-Recursion&batchId=273

def seq(n):
    if n==0:
        return 1
    else:
        return n+n*(seq(n-1))
print(seq(2))

