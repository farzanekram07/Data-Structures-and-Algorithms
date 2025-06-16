# using dictionary method - nlogn 
def zipper():
    list1 = [10, 11, 12]
    index = [1, 0, 2]
    pair = dict(zip(index, list1))
    sorted_items = sorted(pair.items())
    reordered_list = [value for key, value in sorted_items]
    return reordered_list

print(zipper())


# using sort - nlogn|n
def sorting(arr, index):
    paired = []

    for i in range(len(arr)):
        paired.append([index[i], arr[i]])
    paired.sort()

    # reffered to 0 learn python - nested_list
    for i in range(len(arr)):
        arr[i] = paired[i][1]

arr = [10, 11, 12]
index = [1, 0, 2]
sorting(arr, index)
print(" ".join(map(str, arr)))


# using extra space - n|n
def beautifulArr(arr, index):
    reordered = [0] * len(arr)

    for i in range(len(arr)):
        reordered[index[i]] = arr[i]

    return reordered


arr = [10, 11, 12]
index = [1, 0, 2]
print(beautifulArr(arr, index))