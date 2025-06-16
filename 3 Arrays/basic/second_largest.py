# using sort - O(nlogn + n)|O(1)

def second_largest(arr):
    n = len(arr)
    arr.sort()   # O(nlogn)

    for i in range(n-2, -1, -1):  # O(N)
        if arr[i] != arr[n-1]:
            return arr[i]
    return -1

arr = [8, 8,-3, 8]
print(second_largest(arr))


# using two pass - O(2*N)|O(1)

def second_largest(arr):
    largest = -1
    second_largest_element = -1

    for i in range(len(arr)): 
        if arr[i] > largest:
            largest = arr[i]

    for i in range(len(arr)):
        if arr[i] > second_largest_element and arr[i] != largest:
            second_largest_element = arr[i]

    return largest, second_largest_element

arr = [10, 20, 30, 40, 50, 60]
print(second_largest(arr))


# using single pass - O(N)|O(1)

def second_large(arr):
    largest = -1
    second_largest_element = -1

    for i in range(len(arr)): 
        if arr[i] > largest:
            second_largest_element = largest
            largest = arr[i]
        elif arr[i] < largest and arr[i] > second_largest_element:
            second_largest_element = arr[i]

    return largest, second_largest_element

arr = [10, 20, 30, 40, 50, 60]
print(second_large(arr))