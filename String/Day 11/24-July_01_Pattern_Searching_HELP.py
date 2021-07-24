# Completed by HELP

# Method You can Apply

# Apply find method from which you can find the first position of pattern
# and futher apply a while loop from first position and increase index of searching every time


# text=input("Enter Text")
# patter=input("Enter pattern you want to search")
text="geeks for geeks"
pattern="geeks"
pos=text.find(pattern)
while pos>=0:
    print(pos)
    pos=text.find(pattern,pos+1)