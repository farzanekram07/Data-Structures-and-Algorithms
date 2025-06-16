# recursive - O(N)|O(N)
# pending


# iterative - O(N)|O(1)

def largest_element(arr):
    if not arr:
        return None
    
    largest = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > largest:
            largest = arr[i]
    return largest

arr = [1, 9, 5, 7, 3]
print(largest_element(arr))


# Two Pointer

def largest(arr):
    if not arr:
        return None
    
    left, right = 0, len(arr)-1
    largest = arr[left]

    while left <= right:
        if arr[left] > largest:
            largest = arr[left]
        if arr[right] > largest:
            largest = arr[right]
        left += 1
        right -= 1
    
    return largest


arr = [1, 19, 5, 7, 3]
print(largest(arr))



# using Library - O(N)|O(1)

def large(arr):
    return max(arr)

arr = [10, 40, 20, 30]
print(large(arr))
