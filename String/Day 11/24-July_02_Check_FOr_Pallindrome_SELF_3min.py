# 24 July 08:00AM-08:03AM 3 min Completed by SELF
# Short Trick Chceck Reverse of string to actual string

s="abba"
if(s[::]==s[::-1]):
    print("Yes")
else:
    print("No")

# 24 July 08:04AM-08:12AM 4 min Completed by HELP
# ----Another Mehod----
# We can assign low as first index and high as last index 
# Compare low with high if both have not eqaul value then  print no else increase the low and decrease hight till we get low > high


s="10022001"
low=0
high=len(s)-1
while low<high:
    if(s[low]!=s[high]):
        print("NO")
        break
    low+=1
    high-=1
else:
    print("YES")