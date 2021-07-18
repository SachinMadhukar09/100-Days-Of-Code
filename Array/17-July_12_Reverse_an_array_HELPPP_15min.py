# Completed HELPPPPPPPP 15min




a=[1,1,2,2,3,3]
n=len(a)
s=0
for i in range(n):
    if s<n:
        a[s],a[n-1]=a[n-1],a[s]
        s+=1
        n-=1
print(a)
    
    