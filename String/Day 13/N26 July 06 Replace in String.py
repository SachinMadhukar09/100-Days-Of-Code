# 26 July 08:00AM-08:10AM Not Completd 10min

# Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor',
# replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.

# ------My Code-----
s='The lyrics is not that poor!'
l=s
a=s.find('not that poor')
print(a)
r=l.replace(s[:a],'good')
# newl=s+r
print(r)


# ----------Code by Help------
def not_poor(str1):
  snot = str1.find('not')
  spoor = str1.find('poor')
  

  if spoor > snot and snot>0 and spoor>0:
    str1 = str1.replace(str1[snot:(spoor+4)], 'good')
    return str1
  else:
    return str1
print(not_poor('The lyrics is not that poor!'))
print(not_poor('The lyrics is poor!'))