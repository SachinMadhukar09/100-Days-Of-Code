def isZeroSum(l):
    pre_sum=0
    h=set()
    for i in range(len(l)):
        pre_sum+=l[i]
        if pre_sum==0 or pre_sum in h:
            return True
        h.add(pre_sum)
    return False
l=[97, -27 ,2 ,-34 ,61 ,-39]
print(isZeroSum(l))