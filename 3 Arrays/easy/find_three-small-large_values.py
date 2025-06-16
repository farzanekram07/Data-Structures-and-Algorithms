import heapq

# O(n logn)
def find_three_small_values1(arr):
    new_arr = sorted(arr)[:m]
    return new_arr

# O(n logk)
def find_three_small_values2(arr):
    new_arr = heapq.nsmallest(3, arr)
    return new_arr

# O(n)
def find_three_small_values3(arr):
    min1 = min2 = min3 = float('inf')
    
    for num in arr:
        if num < min1:
            min3 = min2
            min2 = min1
            min1 = num
        elif num < min2:
            min3 = min2
            min2 = num
        elif num < min3:
            min3 = num

    new_arr = [min1, min2, min3]
    return new_arr

arr = [7, 3, 2, 4, 9, 12, 56]
m = 3
print(find_three_small_values1(arr))
print(find_three_small_values2(arr))
print(find_three_small_values3(arr))

