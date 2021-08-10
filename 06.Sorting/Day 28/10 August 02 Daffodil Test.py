n=int(input())
l=list(map(int,input().split(" ")))
t=int(input())
for i in range(n):
    for j in range(n):
        if l[i]+l[j]==t:
            print(i,j)