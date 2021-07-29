# 29 July 07:35AM-07:38AM
#               Logic 2min
#               Coding 1min

# Python program to count number of vowels using sets in given string
# Last Updated : 18 Dec, 2019
# Given a string, count the number of vowels present in given string using Sets.

# Prerequisite: Sets in Python

# Examples:

# Input : GeeksforGeeks
# Output : No. of vowels : 5

# Input : Hello World
# Output : No. of vowels :  3

# ---My Approach is same as GFG ---

# Approach:
# 1. Create a set of vowels using set() and initialize a count variable to 0.
# 2. Traverse through the alphabets in the string and check if the letter in the string is present in set vowel.
# 3. If it is present, the vowel count is incremented.

# Below is the implementation of above approach:

s="Sachin"
c=0
vowels=set("aeiouAEIOU")
for i in s:
    if i in vowels:
        c+=1
print(c)

