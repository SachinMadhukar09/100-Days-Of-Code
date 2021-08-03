def printnto1(n):
    if n<=0:
        return 0
    print(n)
    printnto1(n-1)
n=9
print(printnto1(n))