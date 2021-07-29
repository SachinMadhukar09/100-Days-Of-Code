# 25 july 07:40Am-08:00AM 20min Not Completed
# 25 july 06:10Am-06:40AM 30min Not Completed


# Realize that it is DP problem same as Longest Pallindrome

# Link https://practice.geeksforgeeks.org/problems/longest-repeating-subsequence2004/1

a="aabebcdd"
b="aabebcdd"
t=[[]]
for i in range(len(a)-1):
    for j in range(len(b)-1):
        if(a[i-1]==b[j-1] and i!=j ):
            t[i][j]=t[i-1][j-1]+1
        else:
            t[i][j]=max(t[i][j-1],t[i-1][j-1])
            
    
s="aaaabbaa"    
low,high,start,end=0,0,0,1
for i in range(len(s)):
    # For Even
    if(len(s)%2==0):
        low,high=i,i+1
        while( low>=0 and high<len(s) and s[low]==s[high]):
            if(high-low+1>end):
                start=low
                end=high-low+1
            low-=1
            high+=1
    # For Odd String    
    
    if(len(s)%2==0):
        low,high=i,i+2
        while( low>=0 and high<len(s) and s[low]==s[high]):
            if(high-low+1>end):
                start=low
                end=high-low+1
            low-=1
            high+=1