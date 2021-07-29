# 29 July 06:38AM-06:52AM
#               Logic 4min
#               Coding 10min

# Python program to capitalize the first and last character of each word in a string
# Last Updated : 30 Jan, 2020
# Given the string, the task is to capitalise the first and last character of each word in a string.

# Examples:

# Input: hello world
# Output: HellO WorlD

# Input: welcome to geeksforgeeks
# Output: WelcomE TO GeeksforgeekS

# -------My Logic-------

# s="This is my Day"
# ns=s.split(' ')
# ns.title()
# n=len(s)
# ns[n-1].upper()
# print(ns)

# -----It Does not Work------

# -----From GFG------
# Approach:

# Access the last element using indexing.
# Capitalize the first word using title() method.
# Then join the each word using join() method.
# Perform all the operations inside lambda for writing the code in one-line.

s = "This is my Day"
print(' '.join(map(lambda s: s[:-1]+s[-1].upper(), s.title().split())))

# return ' '.join(map(lambda s: s[:-1]+s[-1].upper(),
#                         s.title().split()))
