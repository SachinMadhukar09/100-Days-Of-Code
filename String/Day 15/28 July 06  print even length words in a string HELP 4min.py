# 28 July 08:26PM-08:31PM
        # Logic 2min
        # Coding 2min

# Python program to print even length words in a string
# Difficulty Level : Easy
# Last Updated : 26 Oct, 2018
# Given a string. The task is to print all words with even length in the given string.

# Examples:

# Input: s = "This is a python language"
# Output: This
#         is
#         python
#         language 

# Input: s = "i am muskan"
# Output: am
#         muskan

s = "This is a python language"
s=s.split(' ')
for i in s:
    if len(i)%2==0:
        print(i)