# 07 August 07:32AM-07:40AM 8min
# SELF   # GFG
#                  Logic    1min      5min
#                  Coding   0min      2min

def squareroot(x):
    if x == 0 or x == 1:
        return x
    i, result = 1, 1
    while result <= x:
        i += 1
        result = i*i
    return i-1
print(squareroot(9))
