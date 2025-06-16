# iterative - O(N2)|O(N)

def remove_duplicates(arr):
    n = len(arr)
    res = []

    for i in range(len(arr)):
        if arr[i] not in res:
            res.append(arr[i])
    return res

arr = [1, 5, 5, 3, 2, 2]
print(remove_duplicates(arr))


# iterative - O(N)|O(N)

def remove(arr):
    n = len(arr)
    res = set()

    for i in range(len(arr)):
        if arr[i] not in res:
            res.add(arr[i])
    return res

arr = [1, 5, 5, 3, 2, 2]
print(remove(arr))


# Expected iterative - O(N)|O(1)

def removing_duplicates(arr):
    n = len(arr)
    if n <= 1:
        return n
    
    idx = 1
    
    for i in range(1, n):
        if arr[i] != arr[i-1]:
            arr[idx] = arr[i]
            idx += 1
    return idx

arr = [1, 5, 5, 3, 2, 2]
result = removing_duplicates(arr)

for i in range(result):
    print(arr[i], end = " ")
print()
