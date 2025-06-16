# using counting sort
# O(n+k)|O(k)
# for all non- negative number 
def countArr(arr):
    if not arr:
        return arr
    
    # why max? because it will help to make a 
    # count(which is frequency list) list 
    max_val = max(arr)

    # this freq list help to count the occurence of number
    count = [0] * (max_val+1)

    for i in arr:
        count[i] += 1

    print(count)

    # reconstruct the actual sorted array using count list
    sorted_arr = []
    for num, freq in enumerate(count):
        sorted_arr.extend([num] * freq)
    return sorted_arr

arr = [4, 2, 2, 8, 3, 3, 1]
print(countArr(arr)) 



# efficient for positive and negative both
# instead 0 to max - we go with (min to max)
def counting_sort_with_negatives(arr):
    if not arr:
        return arr

    min_val = min(arr)
    max_val = max(arr)

    # Range of elements - min to max
    range_of_elements = max_val - min_val + 1

    count = [0] * range_of_elements

    # Store the count of each element
    for num in arr:
        count[num - min_val] += 1

    # Reconstruct the sorted array
    sorted_arr = []
    for i in range(range_of_elements):
        sorted_arr.extend([i + min_val] * count[i])
    return sorted_arr

arr = [-5, -10, 0, -3, 8, 5, -1, 10]
print("Original:", arr)
print("Sorted:  ", counting_sort_with_negatives(arr))



# where cyclic sort is optimal solution here
