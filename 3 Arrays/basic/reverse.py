# iterative - using temp arr - O(N)|O(N)

def reversi(arr):
    n = len(arr)
    rev_arr = []

    for i in range(n, 0, -1):
        rev_arr.append(i)
    return rev_arr

arr = [1, 2, 3, 4, 5]
print(reversi(arr))

          

# iterative - using two pointers - O(N)|O(1)

def reverse_array(arr):
    left = 0
    right = len(arr) - 1
    
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr

arr = [1, 2, 3, 4, 5]
print(reverse_array(arr))



# iterative - O(N)|O(1)

def reversing(arr):
    n = len(arr)
    mid = n // 2

    j = -1
    for i in range(mid):
            arr[i], arr[j] = arr[j], arr[i]
            j -= 1
    return arr

arr = [1, 2, 3, 4, 5]
print(reversing(arr))