def segregate(arr):
    zero_count = 0
    one_count = 0
    for i in arr:
        if i == 0:
            zero_count += 1
        else:
            one_count += 1
    return [0] * zero_count + [1] * one_count


def segregate1(arr):
    list = []
    for i in arr:
        if i == 0:
            list.insert(0, i)
        else:
            list.append(i)
    return list


#  binary sort - O(nlogn )|O(1)
def segregation2(arr):
    low = 0
    high = len(arr) - 1

    while low < high:
        if arr[low] == 1:
            if arr[high] != 1:
                arr[low], arr[high] == arr[high], arr[low]
                low += 1
                high -= 1
            else:
                high -= 1
        else:
            low += 1

arr = [1, 0, 0, 0, 1, 1, 0, 0, 0]
print(segregate(arr))
print(segregate1(arr))
segregation2(arr)
print(arr)



