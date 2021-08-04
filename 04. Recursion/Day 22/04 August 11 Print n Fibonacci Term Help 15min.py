# 03 August 06:08AM-07:23AM 15min 
                          # SELF    #GFG    
#                  Logic    8min    2min
#                  Coding   0min    5min

# Link - https://practice.geeksforgeeks.org/problems/fibonacci-using-recursion/1/?track=DS-Python-Recursion&batchId=273

def Fibonacci(n):
    if n<0:
        return ("Incorrect Term")
    elif n==0:
        return 0
    elif n==1:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)
print(Fibonacci(20))