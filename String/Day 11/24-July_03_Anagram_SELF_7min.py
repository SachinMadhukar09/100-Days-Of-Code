# 24 July 08:15AM-08:22AM 7min Completed by Self
#Method
# first iterate all element of first string and second string ,
# store the unicode of all element in seperate array and 
# Compare both array after sorting if true then yes otherwise No

a="listen"
b="silent"
d=[]
e=[]
for i in a:
    d.append(ord(i))
d.sort()
# print(d)
for j in b:
    e.append(ord(j))
e.sort()
# print(e)
if(d==e):
    print("YES")
else:
    print("NO")
    
    
#----------Another Method------------
# Method
# first check the lenght of both string
# sort both string and compare then return

# time Complexity : O(nlogn)
# By HELP

def areAnagram(s1,s2):
    if len(s1)!=len(s2):
        return False
    s1=sorted(s1)
    s2=sorted(s2)
    return (s1==s2)
s1="listen"
s2="silent"
print(areAnagram(s1,s2))

#----------Another Method------------
# Method
# first check the lenght of both string
# assign a array of 256 lenght with 0 value
# run a loop for thr range of any string
# increase the value of index of letter in the array by 1 for s1
# decrease the value of index of letter in the array by 1 for s2
# if final value of array is 0 return true

# time Complexity : O(n)
# By HELP
    
    
def areAnagram(s1,s2):
    if(len(s1)!=len(s2)):
        return False
    count=[0]*256
    for i in range(len(s1)):
        count[ord(s1[i])]+=1
        count[ord(s2[i])]-=1
    for x in count:
        if x!=0:
            return False
    return True
s1="silent"
s2="listen"
print(areAnagram(s1,s2))
        
    