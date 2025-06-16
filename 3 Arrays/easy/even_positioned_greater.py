
def even_positioned_greater(arr):
    
    for i in range(len(arr)):
        if (i+1) % 2 == 0:
            if i > 0 and arr[i] < arr[i-1]:
                arr[i], arr[i-1] = arr[i-1], arr[i]
        else:
            if i+1 < len(arr) and arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr

arr = [1, 2, 2, 1]
print(even_positioned_greater(arr))
print(even_positioned_greater([3, 1, 4, 1, 5, 9]))  # Expected: [1, 3, 1, 4, 5, 9]
print(even_positioned_greater([9, 6, 8, 3, 7]))  # Expected: [6, 9, 3, 8, 7]




# copy from gfg - O(N)|O(N)
def rearrangeArray(arr):
    n = len(arr)

    for i in range(1, n):
        if (i + 1) % 2 == 0:
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
        else:
            if arr[i] > arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]

    return arr


if __name__ == "__main__":

    inputArray = [1, 2, 2, 1]

    resultArray = rearrangeArray(inputArray)

    print(" ".join(map(str, resultArray)))
