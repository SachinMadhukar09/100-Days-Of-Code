# 26 July 07:19AM-07:29AM Completed by HELP 10 min


# ----My Code----
s="restart"
l=list(s)
for i in range(len(l)):
    for j in range(0,i+1):
        if l[i]==l[j]:
            l[j]=='$'
print(l)

# ----Code by help------
s="restart"
c=s[0]
s=s.replace(c,'$')
s=c+s[1:]
print(s)