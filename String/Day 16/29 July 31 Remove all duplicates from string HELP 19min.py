# 29 July 05:10PM-05:29PM 19min 
                          # SELF    GFG
#                  Logic    5min    5min 
#                  Coding   4min    5min

# Remove all duplicates from a given string in Python
# Difficulty Level : Easy
# Last Updated : 22 Nov, 2020
# We are given a string and we need to remove all duplicates from it? What will be the output if the order of character matters?
# Examples:

# Input : geeksforgeeks
# Output : efgkos

# -------Mine Approach--------

# s="geeksforgeeks"
# c=[0]*256
# d=[]
# for i in s:
#     c[ord(i)]+=1
# # print(c)
# for j in c:
#     if (c[j]==1):
#         print(j)
#         d.append(i)
# print(d)


# -------GFG Approach--------

str="geeksforgeeks"
s=list(str)
n=len(s)
index=0
for i in range(n):
    for j in range(i+1):
        if s[i]==s[j]:
            break
    if i==j:
        s[index]=s[i]
        index+=1
# print(s[:index])
d=s[:index]
d.sort()
# print(d)
print(''.join(d))


