def dSum(n):
    if n<10:
        return n
    return dSum(n//10)+n%10
print(dSum(253))