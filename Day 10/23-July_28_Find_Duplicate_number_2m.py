# Link https://leetcode.com/problems/find-the-duplicate-number/

# 23-July 07:05AM-07:10AM 5 min Completed by HELP


def findDuplicate(nums):
        D={}
        for i in nums:
            if i not in D:
                D[i]=1
            else:
                return i
nums=[1,3,4,2,2]
print(findDuplicate(nums))