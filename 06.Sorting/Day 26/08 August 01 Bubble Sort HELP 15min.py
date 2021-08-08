# 08 August 06:38AM-06:53AM 15min
                               # GFG
#                  Logic         13min
#                  Coding        2min 

# Time Complexity - O(n^2)

def bubblesort(l):
    n=len(l)
    for i in range(n-1):
        for j in range(n-i-1):
            if l[j]>l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]
    return l
l=[10,8,20,5]
print(bubblesort(l))


# -----Optimized Solution-----
def bubblesort(l):
    n=len(l)
    for i in range(n-1):
        swapped=False
        for j in range(n-i-1):
            if l[j]>l[j+1]:
                l[j],l[j+1]=l[j+1],l[j]
                swapped=True
        if swapped==False:
            return 
    return l
l=[10,8,20,5]
print(bubblesort(l))

