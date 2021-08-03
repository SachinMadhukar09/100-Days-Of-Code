# 03 August 06:33PM-06:38AM 5min 
                          # SELF    
#                  Logic    3min     
#                  Coding   2min    

# Link - https://practice.geeksforgeeks.org/problems/print-1-to-n-without-using-loops-1587115620/1/?track=DS-Python-Recursion&batchId=273


def fun(n):
    if n==0:
        return 
    print(n)
    return fun(n-1)
n=int(input())
print(fun(n))