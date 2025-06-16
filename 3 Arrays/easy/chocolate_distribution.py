# finding the first the small value in arr using heapq
# then find the difference between max and min of new_arr
# bt it can't find the min of all array
# Easliy solves using sliding window technique

import heapq

def distribution(arr):
    new_arr = heapq.nsmallest(3, arr)
    diff = new_arr[-1] - new_arr[0]
    return diff

arr = [7, 3, 2, 4, 9, 12, 56]
print(distribution(arr))



# here comes the sliding window 

def find_min_diff(arr, m):
    if m == 0 or len(arr) < m:
        return 0
    arr.sort()
    min_diff = float('inf')
    for i in range(len(arr) - m + 1):
        current_window = arr[i: i + m]
        current_diff = current_window[-1] - current_window[0]
        min_diff = min(min_diff, current_diff)
        print(f"Window: {current_window}, Difference: {current_diff}")
    return min_diff

arr = [7, 3, 2, 4, 9, 12, 56]
m = 3
result = find_min_diff(arr, m)
print(f"Minimum difference is: {result}")
