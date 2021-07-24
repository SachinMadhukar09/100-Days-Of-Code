print("---Unicode")
print(ord('a'))
print(ord('A'))
print(chr(97))
print(chr(65))
print()

print("---Formatted String in Python")

print("1.Like C Language")

name="Sachin"
course="Python Course"
s="Welcome %s to the %s" %(name,course)
print(s)
print()

print("2.Using Function")
name="Sachin"
course="Python Course"
s="Welcome {0} to the {1}" .format(name,course)
print(s)
print()

print("3.Using f-String")

# Example 1

name="Sachin"
course="Python Course"
s=f"Welcome {name} to the {course}"
print(s)
print()

# Example 2
# We can use expression with f-String
a,b=10,20
print(f"Sum of {a} and {b} is {a+b}")
print(f"Product of {a} and {b} is {a*b}")
print()

# Example 3
# We can call Method with f-String

s1="ABC"
s2="abc"
print(f"Lower Case of {s1} is {s1.lower()}")
print(f"Upperr Case of {s2} is {s2.upper()}")
print()

# ----String Operation-------- 
# 1.Checkin Substring

print("String Operation")
print("1.Checking Substring")
s1="geeksforgeeks"
s2="geeks"
print(s2 in s1)
print(s2 not in s1)
print()

# 2.Concatenation

print("2.Concatenation")
s1="geeks"
s2="forgeeks"
s3=s1+s2
s4="Welcome to "+s1+s2
s5="Welocme to "+s3
print(s3)
print(s4)
print(s5)
print()

# ----String Methods-------- 
#  3.Finding position of substrings
# i.Index Method

print("------String Methods-------")
print(" 3.Finding position of substrings")
print("i.Index Method")
  
s1="geeksforgeeks"
s2="geeks"
print(s1.index(s2)) # First index of s2
print(s1.rindex(s2)) # Last index of s2
print(s1.index(s2,0,13)) # same as first search is begin from index 0
print(s1.index(s2,1,13)) # search is begin from index 1
print()

# 4.Len Method

print("4.Len Method")
s1="geeks"
print(len(s1))
print()

# 5. Lower and Upper Method

print("5. Lower and Upper Method")
s1="Geeks"
s2=s1.upper()
print(s2)
s3=s1.lower()
print(s3)
print(s2.isupper())
print(s1.islower())
print()

# 6.Starts with or end with Method

print("6.Starts with or end with")

s="GeeksforGeeks Pyhton Course"
print(s.startswith("Geeks"))
print(s.endswith("Course"))
print(s.startswith("Geeks",1))
print(s.startswith("Geeks",8,len(s)))
print()
 
# 7.Split and Join Methood

print("Split and Join Method")
s1=" geeks for geeks"
print(s1.split())
s2="geeks, for , geeks"
print(s2.split(","))
l=["geeksforgeeks","pyhton","course"]
print("".join(l))
print(",".join(l))
print()

# 8. strip , lstrip ,rstrip methods
# this is used to remove unwanted characters from corner of string
print("8.strip , lstrip ,rstrip methods")
# this can work without parameter , it remove wide spaces
print("this can work without parameter , it remove wide spaces")
print()
print("--strip")
# this can remove wide spaces or any parameter from both side
print("this can remove wide spaces or any parameter from both side")
s=" geeksforgeeks   "
print(s)
print(len(s))
g=s.strip()
print(len(g))
print(s.strip())
print()
s="--geeksforgeeks---"
print(s)
print(len(s))
g=s.strip("-")
print(len(g))
print(s.strip("-"))
print()


print("--rstrip")
# this remove wide spaces or any parameter from left side only
print("this remove wide spaces or any parameter from right side only")
s=" geeksforgeeks   "
print(s)
print(len(s))
g=s.rstrip()
print(len(g))
print(s.rstrip())
print()

s="--geeksforgeeks---"
print(s)
print(len(s))
g=s.rstrip("-")
print(len(g))
print(s.rstrip("-"))
print()

print("--lstrip")
# this remove wide spaces or any parameter from left side only
print("this remove wide spaces or any parameter from left side only")
print()

s=" geeksforgeeks   "
print(s)
print(len(s))
g=s.lstrip()
print(len(g))
print(s.lstrip())
print()

s="--geeksforgeeks---"
print(s)
print(len(s))
g=s.lstrip("-")
print(len(g))
print(s.lstrip("-"))
print()

# 9.Find Method
print("9.Find Method")
# this is same as index method there is difference 
# if we use index methos then if the element is not present then it gives error 
# if we use find method then if the element is not present then it returns -1
print("""this is same as index method there is difference 
if we use index methos then if the element is not present then it gives error 
if we use find method then if the element is not present then it returns -1""")
print()
s1="geeks for geeks"
s2="geeks"
s3="Sachin"
print(s1.find(s2))
print(s1.find(s3))
print(s1.find("gfg"))
n=len(s1)
print(s1.find(s2,1,n))
