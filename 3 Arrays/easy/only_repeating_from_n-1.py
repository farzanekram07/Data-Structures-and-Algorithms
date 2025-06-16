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
                return arr[i]

def sorting(arr):
    arr.sort()
    for i in range(len(arr)):
        if arr[i] == arr[i + 1]:
            return arr[i]
        
def hashset(arr):
    data = set()
    for i in arr:
        if i in data:
            return i
        data.add(i)
    return -1

def visited_array(arr):
    n = len(arr)
    hashset = [0] * (n+1)

    for i in arr:
        hashset[i] += 1

        if hashset[i] > 1:
            return i

def formula(arr):
    n = len(arr)

    expected_sum = ((n-1) * n // 2)
    total_sum = sum(arr)
    duplicate = total_sum - expected_sum
    return duplicate

arr = [6, 2, 2, 3, 4, 1, 5]
print(repetitive_element(arr))
print(sorting(arr))
print(hashset(arr))
print(visited_array(arr))
print(formula(arr))