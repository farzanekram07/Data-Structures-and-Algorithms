
def distinct_elements(arr):
    lst = set(arr)
    return list(lst)

arr = [1, 1, 2, 3, 2, 3, 1, 4]
print(distinct_elements(arr))