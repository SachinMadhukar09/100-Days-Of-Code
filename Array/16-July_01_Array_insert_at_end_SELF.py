# Completed  By Self

# 1. Array insert at end 
# Basic Accuracy: 67.88% Submissions: 18458 Points: 1
# Insertion is a basic but frequently used operation. Arrays in most languages can not be dynamically shrinked or expanded. Here, we will work with such arrays and try to insert an element at the end of the array.

# You are given an array arr. The size of the array is given by sizeOfArray. You need to insert an element at the end.

# Example 1:

# Input:
# sizeOfArray = 6
# arr[] = {1, 2, 3, 4, 5}
# element = 90
# Output: 1 2 3 4 5 90
# Explanation: After inserting 90 at the
# end, we have array elements as 
# 1 2 3 4 5 90.
# Example 2:

# Input:
# sizeOfArray = 4
# arr[] = {1, 2, 3}
# element = 50
# Output: 1 2 3 50
# Explanation: After inserting 50 at the 
# end, we have array elements as 
# 1 2 3 50.

def insertAtEnd(arr,element):
    arr.append(element)
    return arr

arr=[1,2,3,4]
element=5
print(insertAtEnd(arr,element))
