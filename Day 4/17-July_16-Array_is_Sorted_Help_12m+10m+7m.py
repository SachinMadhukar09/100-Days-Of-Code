# 17 July Not Completed 11:42AM-11:54AM 12min
# 18 July Not Completed 09:00AM-09:10AM 10min
# 19 July Not Completed 09:00AM-09:07AM 7min


# a = [4, 24, 52, 5]
# a=[1,2,3,4]
# a=[49 ,80 ,67 ,13 ,13 ,1 ,71 ,83 ,51 ,13, 45]
# b=a.sort()
# if(a==b):
#     print("yes")
# else:
#     print("No")
# n = len(a)
# for i in range(n):
#     if(a[i] <= a[i-1]):
#         print("Yes")
#         break
#     else:
#         print("No")


# ---------Prashant Code--------

def arrayisSorted(arr,n):
    for i in range(n-1):
        if(arr[i]>arr[i+1]):
            return False
    return True
arr=[1,4,6,3,5]
n=len(arr)
print(arrayisSorted(arr,n))



# -----------------Logic

# a=[1,4,5,2,5]
# b=a
# b.sort()
# print(a)
# print(b)


# In this code the output is same for both Why?
   # Because b act as pointer of a , whenever we copy the element to another variable then it will act a spointer of first one
   
   