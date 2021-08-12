# 09 August 06:15AM-37:AM 22min
# GFG
#                  Logic         12min
#                  Coding        10min

def mergeSubarray(a, low, mid, high):
    left = a[low:mid+1]
    right = a[mid+1:high+1]
    i, j, k = 0, 0, low
    print(left)
    print(right)
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            a[k] = left[i]
            k = k+1
            i = i+1
        else:
            a[k] = right[j]
            k = k+1
            i = i+1
    while i < len(left):
        a[k] = left[i]
        k = k+1
        i = i+1
    while j < len(right):
        a[k] = right[j]
        k = k+1
        j = j+1
    print(a)


a = [10, 15, 20, 40, 8, 11, 55]
low = 0
mid = 3
high = 6
print(mergeSubarray(a, low, mid, high))
