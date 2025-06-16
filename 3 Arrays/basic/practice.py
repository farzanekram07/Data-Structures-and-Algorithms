# Given an array of size n filled with numbers from 
# 1 to n-1 in random order. The array has only one 
# repetitive element. The task is to find the repetitive element.

# Examples:
# Input: a[] = [1, 3, 2, 3, 4]
# Output: 3


# brute force 
def repetitive_element(arr):
    for i in range(len(arr)):
        for j in range(1, len(arr)):
            if arr[i] == arr[j]:
                return i
            
arr = [1, 1, 2, 3, 4, 5]
print(repetitive_element(arr))