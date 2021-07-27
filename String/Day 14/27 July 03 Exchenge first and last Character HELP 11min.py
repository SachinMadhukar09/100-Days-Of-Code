# 27 July 07:12AM-07:23AM Completed by HELP 11min 

# Write a Python program to change a given string to a new string where the first and last chars have been exchanged.

s="thisisgood"
print(s[-1:]+s[1:-1]+s[:1])

# ---------
input="this is good"
output="good is this"
l=input.split()
print(l[-1]+l[1:-1]+l[1])