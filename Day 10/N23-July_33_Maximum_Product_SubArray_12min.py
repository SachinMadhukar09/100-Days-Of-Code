# link https://practice.geeksforgeeks.org/problems/maximum-product-subarray3604/1

# 23-July 05:08PM-05:20PM 12min Not Completed

# a=[2, 3, 4, 5, -1, 0]
a=[6, -3, -10, 0, 2]
max_p=max(a)
p=a[0]
c=[]
for i in range(len(a)):
    d=p*a[i]
    if d>p:
        p=d
        c.append(a[i])
        print(c)
    # else:
    #     p=d
    #     c.append(a[i])
    #     print (c)
print(c)