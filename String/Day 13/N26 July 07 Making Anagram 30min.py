# 26 July 05:35PM-05:55PM 20min Not Completed
# 26 July 06:20PM-06:30PM 10min Not Completed

# a="abd"
# b="bdc"
# d=[]
# e=[]
# s=[]
# q=0
# for i in a:
#     d.append(i)
# d.sort()
# # print(d)
# for j in b:
#     e.append(j)
# e.sort()
# # print(e)
# for k in range(len(e)):
#     for m in range(len(d)):
#         if(m==k):
#             s.append(m)
# print("".join(s))

            
            
# a="abd"
# b="bdc"
a="fcrxzwscanmligyxyvym"
b="jxwtrhvujlmrpdoqbisbwhmgpmeoke"
d=[]
e=[]
s=[]
q=0
for i in a:
    d.append(i)
# d.sort()
for j in b:
    d.append(j)
# e.sort()
print(d)
print(len(d))
# print(e)
for k in range(len(d)):
    for m in range(len(d)):
        if(d[m]==d[k]):
            q+=1
            e.append(d[m])
#             s.append(m)
print(e)
print(q)
# print("".join(s))

            