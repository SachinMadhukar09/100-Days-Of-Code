# 32 July 7:45AM-7:55AM 10min Completed by Help

# -------GFG Code--------

def findTriplets(arr, n):
    found = False
    for i in range(n-1):
        # Find all pairs with sum
        # equals to "-arr[i]"
        s = set()
        for j in range(i+1,n):
            x = -(arr[i] + arr[j])
            if x in s:
                # print(x, arr[i], arr[j])
                found = True
                return 1
            else:
                s.add(arr[j])
    if found == False:
        # print("No Triplet Found")
        return 0

 
# Driver Code
# arr = [0, -1, 2, -3, 1]
# arr = [3, 4, 0, -7, 1]
arr=[63 ,-30 ,4, 13 ,85 ,-6 ,11]
n = len(arr)
print(findTriplets(arr, n))
 
# This code is contributed by Shrikant13