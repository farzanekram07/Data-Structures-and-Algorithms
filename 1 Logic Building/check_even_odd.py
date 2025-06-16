#1 using mod operator
def is_even(arr):
    new_arr = []
    for i in arr:
        if i % 2 == 0:
            new_arr.append(True)
        else:
            new_arr.append(False)
    return new_arr

arr = [1, 2, 3, 4, 5, 6]
print(is_even(arr))


#2 bitwise AND
def even(arr):
    new_arr = []
    for i in arr:
        if i & 1 == 0:
            new_arr.append(True)
        else:
            new_arr.append(False)
    return new_arr

arr = [1, 2, 3, 4, 5, 6]
print(even(arr))


#3 list comprehension
def check_even(arr):
    return list(map(lambda x: x % 2 == 0, arr))

arr = [1, 2, 3, 4, 5, 6]
print(check_even(arr))