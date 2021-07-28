# 28 July 08:20PM-08:25PM
        # Logic 2min
        # Coding 3min

# Python – Avoid Spaces in string length
# Difficulty Level : Easy
# Last Updated : 05 Sep, 2020
# Given a String, compute all the characters, except spaces.

# Input : test_str = ‘geeksforgeeks 33 best’
# Output : 19
# Explanation : Total characters are 19.

# Input : test_str = ‘geeksforgeeks best’
# Output : 17
# Explanation : Total characters are 17 except spaces.

s="This is my Day"
print(sum(not chr.isspace() for chr in s))