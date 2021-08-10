n=int(input())
a=list(map(int,input().split(" ")))
s=0
for i in range(len(a)):
    if len(a)<2:
        break
    elem = max(a[0],a[-1])
    if (i%2==0):
        s+=elem
    a.remove(elem)
print(s)
