# using temp array
def moveZeros1(arr):
    n = len(arr)
    temp = [0] * n
    j = 0

    for i in range(n):
        if arr[i] != 0:
            temp[j] = arr[i]
            j += 1

    while j < n:
        temp[j] = 0
        j += 1

    return temp

arr = [2, 0, 1, 0, 4, 5, 6]
print(moveZeros1(arr))



# two pass 
def moveZeros2(arr):
    n = len(arr)
    j = 0

    for i in range(n):
        if arr[i] != 0:
            arr[j] = arr[i]
            j += 1
        
    while j < n:
        arr[j] = 0
        j += 1

    return arr

arr = [0, 1, 2, 5, 3, 0, 0, 2]
print(moveZeros2(arr))


# single pass
def moveZeros3(arr):
    n = len(arr)
    j = 0

    for i in range(n):
        if arr[i] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
    
    return arr

arr = [0, 1, 3, 0, 0, 2]
print(moveZeros3(arr))