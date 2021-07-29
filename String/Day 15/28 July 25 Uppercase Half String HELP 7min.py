# 28 July 08:33PM-08:40PM
        # Logic 4min
        # Coding 3min

# Python – Uppercase Half String
# Last Updated : 05 Sep, 2020
# Given a String, perform uppercase of later part of string. 

# Input : test_str = ‘geeksforgeek’
# Output : geeksfORGEEK
# Explanation : Latter half of string is uppercased.

# Input : test_str = ‘apples’
# Output : appLES
# Explanation : Latter half of string is uppercased.

s="Sachin"
half_index=len(s)//2
res=''
for i in range(len(s)):
    if i >= half_index:
        res+=s[i].upper()
    else:
        res+=s[i].lower()
print(res)