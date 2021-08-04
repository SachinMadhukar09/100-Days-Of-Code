# 04 August 07:1AM-07:10AM 9min 
                          # SELF    #GFG    
#                  Logic    2min    1min
#                  Coding   0min    6min

# Link - https://practice.geeksforgeeks.org/problems/check-palindrome/1/?track=DS-Python-Recursion&batchId=273

def isPalin(N):
    # code here
    str = 'N'
    for i in range(len(str)//2):
        if str[i] != str[len(str)-i-1]:
            return 1
    return 0


print(isPalin(101))
