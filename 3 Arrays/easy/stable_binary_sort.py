# Given an array arr[] of integers, the task is to partition 
# the array based on even and odd elements. The partition has 
# to be stable, meaning the relative ordering of all even 
# elements must remain the same before and after partitioning, 
# and the same should hold true for all odd elements.

# Examples:
# Input: arr[] = [1, 0, 1, 1, 0, 0]
# Output: [0 ,0 ,0, 1, 1, 1]
# Explanation: All even numbers came before the odd numbers.

# two pointer approach
def binarySort(arr):
    j = 0
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
    return arr

arr = [2, 4, 1, 5, 3, 6]
print(binarySort(arr))

# using list comprehension
def stablePartition(arr):
    evens = []
    odds = []
    for num in arr:
        if num % 2 == 0:
            evens.append(num)
        else:
            odds.append(num)
    return evens + odds

arr = [2, 4, 1, 5, 3, 6]
print(stablePartition(arr))

# in-place rearrangement (while taking care of order)
def binary_sort_stable(arr):
    n = len(arr)
    for i in range(n):
        if arr[i] % 2 == 0:
            j = i
            while j > 0 and arr[j-1] % 2 == 1:
                arr[j], arr[j-1] = arr[j-1], arr[j]
                j -= 1
    return arr

arr = [2, 4, 1, 5, 3, 6]
print(binary_sort_stable(arr))