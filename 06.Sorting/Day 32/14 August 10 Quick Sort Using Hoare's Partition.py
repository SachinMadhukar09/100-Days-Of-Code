def hoarepartition(a, l, h):
    pivot = a[l]
    i = l-1
    j = h+1
    while True:
        i = i+1
        if a[i] < pivot:
            i = i+1
        j = j-1
        if a[j] > pivot:
            j = j-1
        if i >= j:
            return j
        a[i], a[j] = a[j], a[i]


def qsort(a, l, h):
    if l < h:
        p = hoarepartition(a, l, h)
        qsort(a, l, p)
        qsort(a, p+1, h)
    return a


a = [8, 4, 7, 9, 3, 10, 5]
l = 0
h = len(a)-1
print(qsort(a, l, h))

# Time Complexity

# Best Case - Theeta(nlogn)
# Worst Case - Theeta(n^2)
# Average Case - O(nlogn)

# Auxillary Space

# Best Case - Theeta(n)
# Worst Case - Theeta(logn)
# Average Case - Theeta(logn)
