# 31 July 08:15AM-08:25AM Completed By HELP

from collections import Counter;
def isPalPer(s):
    count=Counter(s)
    odd=0
    for freq in count.values():
        if freq%2!=0:
            odd+=1
            if odd>1:
                return False
    return True
s="meyal"
print(isPalPer(s))