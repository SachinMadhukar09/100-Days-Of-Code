# 29 July 07:04AM-07:15AM
#               Logic 3min
#               Coding 8min

# Python | Program to accept the strings which contains all vowels
# Difficulty Level : Basic
# Last Updated : 22 Feb, 2021
# Given a string, the task is to check if every vowel is present or not. We consider a vowel to be present if it is present in upper case or lower case. i.e. ‘a’, ‘e’, ‘i’.’o’, ‘u’ or ‘A’, ‘E’, ‘I’, ‘O’, ‘U’ . 
# Examples : 

# Input : geeksforgeeks
# Output : Not Accepted
# All vowels except 'o' are not present

# Input : ABeeIghiObhkUul
# Output : Accepted
# All vowels are present

# ---My Approach is same as GFG---
# Approach : Firstly, create set of vowels using set() function. 
# Check for each character of the string is vowel or not, if vowel then add into the set s. 
# After coming out of the loop, check length of the set s, if length of set s is equal to the length of the vowels set then string is accepted otherwise not. 

s="anvdvjwrvsfvd"
s.lower()
vowels=set("aeiou")
d=set({})
for i in s:
    if i in vowels:
        d.add(i)
print(d)
if(len(d)==len(vowels)):
    print("String is Accepted")
else:
    print("String is Not Accepted")
    print()
    
