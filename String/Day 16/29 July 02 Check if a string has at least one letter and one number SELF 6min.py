# 29 July 06:54AM-07:00AM
#               Logic 3min
#               Coding 3min

# Python program to check if a string has at least one letter and one number
# Last Updated : 29 Aug, 2020
# Given a string in Python. The task is to check whether the string has at least one letter(character) and one number. Return “True” if the given string full fill above condition else return “False” (without quotes).
# Examples: 

# Input: welcome2ourcountry34
# Output: True

# Input: stringwithoutnum
# Output: False

# ---My Approach is same as GFG---

# Approach:
# The approach is simple we will use loop and two flags for letter and number. 
# These flags will check whether the string contains letter and number. 
# In the end, we will take AND of both flags to check if both are true or not. 
# Letters can be checked in Python String using the isalpha() method and numbers can be checked using the isdigit() method.

from abc import ABCMeta


s="abcd3mdkn"
flag_n="False"
flag_a="False"
for i in s:
    if i.isalpha():
        flag_a=True
    if i.isdigit():
        flag_n=True
print(flag_n and flag_a)