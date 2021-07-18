# Not Completed 11:42Am-11:54AM 12min
# Not Completed 09:00AM-09:10AM 10min

a = [4, 24, 52, 5]
# a=[1,2,3,4]
# a=[49 ,80 ,67 ,13 ,13 ,1 ,71 ,83 ,51 ,13, 45]
# b=a.sort()
# if(a==b):
#     print("yes")
# else:
#     print("No")
n = len(a)
for i in range(n):
    if(a[i] <= a[i-1]):
        print("Yes")
        break
    else:
        print("No")
