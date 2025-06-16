# Given an unsorted array of integers, sort the array into
# a wave array. An array arr[0..n-1] is sorted in wave form 
# if: arr[0] >= arr[1] <= arr[2] >= arr[3] <= arr[4] >= …..

# Example
# Input:  arr[] = {10, 5, 6, 3, 2, 20, 100, 80}
# Output: arr[] = {10, 5, 6, 2, 20, 3, 100, 80} 



# naive appraoch using sorting - O(nlogn)|O(1)
# order will not taken
def sort_in_wave_form(arr):
    n = len(arr)
    arr.sort()

    for i in range(0, n, 2):
        arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr

arr = [10, 5, 6, 3, 2, 20, 100, 80] 
print(sort_in_wave_form(arr))




# Wave Sort with Original Order - O(N)|O(1)
# The idea is all even positioned (at index 0, 2, 4, ..) 
# elements are greater than their adjacent odd elements,
def sort_in_wave_form(arr):
    n = len(arr)
    
    for i in range(0, n, 2):
        if i > 0 and arr[i] < arr[i-1]:
            arr[i], arr[i-1] = arr[i-1], arr[i]

        if i < n-1 and arr[i] < arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr

arr = [10, 5, 6, 3, 2, 20, 100, 80] 
print(sort_in_wave_form(arr))


