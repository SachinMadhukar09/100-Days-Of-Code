# 29 July 07:22AM-07:30AM
#               Logic 7min
#               Coding 1min 


# Python | Count the Number of matching characters in a pair of string
# Difficulty Level : Easy
# Last Updated : 03 Apr, 2020

# Given a pair of non empty strings. Count the number of matching characters in those strings (consider the single count for the character which have duplicates in the strings).

# Examples:

# Input : str1 = 'abcdef'
#         str2 = 'defghia'
# Output : 4 
# (i.e. matching characters :- a, d, e, f)

# Input : str1 = 'aabcddekll12@'
#         str2 = 'bb22ll@55k'
# Output : 5 
# (i.e. matching characters :- b, 1, 2, @, k)

# ---My Approach is same as GFG need some improvisation---

s1="anfnak"
s2="flsdnfl"
c,j=0,0
for i in s1:
    if s2.find(i)>=0 and j==s1.find(i):
        c+=1
    j+=1
print(c)
