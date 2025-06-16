# using in built function - O(n logn)|O(1)

def three_distinct_elements(arr):
    arr.sort()
    return [arr[-1], arr[-2], arr[-3]]

arr = [40, 20, 50, 10, 60, 30, 70]
print(three_distinct_elements(arr))


# iterative - O(N)|O(1)
def three_distinct(arr):
    n = len(arr)
    if n < 3:
        print("Invalid Input!")
        return

    first = second = third = float('-inf')
    for i in range(n):
        if arr[i] > first:
            third = second
            second = first
            first = arr[i]
        elif arr[i] > second and arr[i] != first:
            third = second
            second = arr[i]
        elif arr[i] > third and arr[i] != second and arr[i] != first:
            third = arr[i]
    return [first, second, third]

     

arr = [40, 20, 50, 10, 60, 30, 70]
print(three_distinct(arr))