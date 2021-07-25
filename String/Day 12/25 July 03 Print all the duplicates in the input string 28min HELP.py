# 25 July 06:50AM-07:04AM 14min Completed by HELP Not on GFG
        
# ------Frequency of Characters------
for i in range(97,123):
    c=0
    j=chr(i)
    for l in s:
        if(l==j):
            c+=1
    if(c>1):
        print(j,":",c)
        
        
        
# 25 July 08:15PM-08:26PM 14min Completed by HELP Not on GFG

# # ---------Character with highest occurence---
str="geeksforgeeks"
count = [0] * 256
max = -1
c = []
for i in str:
    count[ord(i)]+=1; 
for i in str:
    if max < count[ord(i)]:
        max = count[ord(i)]
        c = i
print ("Max occurring character is " + c)
        
