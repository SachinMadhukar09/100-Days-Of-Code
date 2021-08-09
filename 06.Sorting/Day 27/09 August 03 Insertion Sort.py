# 09 August 06:10AM-06:25AM 15min
                               # GFG
#                  Logic         12min
#                  Coding        3min 

# time Complexity - O(n^2)

def insertionsort(l):
    for i in range(1,len(l)):
        x=l[i]
        j=i-1
        while j>=0 and x<l[j]:
            l[j+1]=l[j]
            j=j-1
        l[j+1]=x
    return l
l=[20,5,40,60,10,30]
print(insertionsort(l))        