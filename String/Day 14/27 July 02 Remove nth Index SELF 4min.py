# 27 July 07:03AM-07:07AM Completed by SELF 4min

# Write a Python program to remove the nth index character from a nonempty string.

# ------My Code--------

s="This is good as well as very good"
l=s.split()
print(l)
l.pop(3)
print(l)

# -----Solution From Website-------

def remove_char(str, n):
      first_part = str[:n] 
      last_part = str[n+1:]
      return first_part + last_part
print(remove_char('Python', 0))
print(remove_char('Python', 3))
print(remove_char('Python', 5))
