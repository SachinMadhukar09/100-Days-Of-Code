# 05 August 05:09PM-05:12PM 9min 
                          # SELF    #GFG    
#                  Logic    1min    1min
#                  Coding   0min    1min

#Link https://practice.geeksforgeeks.org/problems/gcd-euclid/1/?track=DS-Python-Recursion&batchId=273
def GCD(a,b):
    if a==0:
        return b
    return GCD(b%a,a)
print(GCD(7,8))