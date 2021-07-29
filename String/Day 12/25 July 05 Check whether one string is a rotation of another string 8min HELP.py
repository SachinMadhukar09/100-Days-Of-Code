# 25 July 06:40AM-06:48AM 8min Completed By HELP

s1 = "AACD"
s2 = "ACDA"
if(len(s1)!=len(s2)):
    print("NO")
else:
    temp=s1+s2
    print(temp)
    if(temp.find(s2)==True):
        print("Yes")
    else:
        print("No")