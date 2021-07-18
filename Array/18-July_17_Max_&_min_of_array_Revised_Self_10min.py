#  06:45AM-06:55AM 10min Completed by self

# Maximum and minimum of an array using minimum number of comparisons

def max(a):
    s=0
    q=0
    for i in range(len(a)-1):
        if(a[i]>a[i+1]):
            q=a[i]
        else:
            q=a[i+1]
        if(q>s):
            s=q
    return s

def min(a):
    s=a[0]
    q=0
    for i in range(len(a)-1):
        if(a[i]>a[i+1]):
            q=a[i+1]
        else:
            q=a[i]
        if(q<s):
            s=q
        return s
    
a=[4,23,5,7,8]
print(max(a))
print(min(a))    