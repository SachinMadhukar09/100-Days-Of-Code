# 28 July 06:55AM-7:15AM Completed by HELP 25min

s="amaama"
n=len(s)
if(s[::]==s[::-1]):
    print("Pallindrome")
else:
    print("NOT Pallindrome")
    
# --------My Code-------
    
# def symmetry(s):
#     n=len(s)
#     flag=0
#     if(n%2==0):
#         mid=n//2+1
#     else:
#         mid=n//2
#     start1=0
#     start2=mid
#     while (start1<mid and start2<n):
#         if(s[start1]==s[start2]):
#             start1+=1
#             start2+=1
#         else:
#             flag=1
#     if(flag==0):
#         print("Symmetrical")
#     else:
#         print("Not Symmetrical")
#     # print("YES")
# s="khokho"    
# print(symmetry(s))

# --------GFG Code-------

def symmetry(a):
    n = len(a)
    flag = 0
    if n%2:
        mid = n//2 +1
    else:
        mid = n//2
    start1 = 0
    start2 = mid
    while(start1 < mid and start2 < n):
        if (a[start1]== a[start2]):
            start1 = start1 + 1
            start2 = start2 + 1
        else:
            flag = 1
            break
    if flag == 0:
        print("The entered string is symmetrical")
    else:
        print("The entered string is not symmetrical")
          
# Driver code
string = 'amaama'
# palindrome(string)
symmetry(string)

