# 25 july 07:15PM-08:15PM 60min Not Completed

# Link https://practice.geeksforgeeks.org/problems/longest-palindrome-in-a-string3411/1

# S = "fyfvladzpbfudkklrwq"
S="aaaabbaa"
low, high, start, end = 0, 0, 0, 1
for i in range(1, len(S)):
    # //even substring
    if(len(S) % 2 == 0):
        l = i
        h = i+1
        while(l > 0 and h < len(S) and S[l] == S[h]):
            if(h-l+1 > end):
                start = l
                end = h-l+1
            l -= 1
            h += 1
     # Odd Substring
    else:
        l=i
        h=i+2
        while(l>0 and h<len(S) and S[l]==S[h]):
            if(h-l+1>end):
                start=l
                end=h-l+1
            l-=1
            h+=1
print(S[start:start + end+2])
