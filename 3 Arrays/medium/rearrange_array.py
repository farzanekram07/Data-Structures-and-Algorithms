# 2149 - Leetcode problem

# My code worked but TC worst, but most important worked
# O(N2)|O(N) 
def rearrange_array(arr):
    new_arr = []

    for i in range(len(arr)):
        if i in arr:
            new_arr.append(i)
        else:
            new_arr.append(-1)
    return new_arr

arr = [-1, -1, 6, 1, 9, 3, 2, -1, 4, -1]
print(rearrange_array(arr))


# O(N2)|O(1)
def modifyArr(arr, n):

    for i in range(n):
        for j in range(n):
            if arr[j] == i:
                arr[j], arr[i] = arr[i], arr[j]

    for i in range(n):
        if arr[i] != i:
            arr[i] = -1

    for i in range(n):
        print(arr[i], end = " ")
    print()

ar = [ -1, -1, 6, 1, 9, 3, 2, -1, 4, -1 ]
n = len(ar)
 
modifyArr(ar, n)


# O(N)|O(N)
def modifyArr2(arr):
    n = len(arr)
    vect = [-1] * n

    for i in range(n):
        if arr[i] != -1:
            vect[arr[i]] = arr[i]

    return vect

arr = [-1, -1, 6, 1, 9, 3, 2, -1, 4, -1]
print(modifyArr2(arr))



# O(N)|O(1)
def modifyArr3(arr):
    i = 0

    while i < len(arr):
        if arr[i] != -1 and arr[i] != arr[arr[i]]:
            temp = arr[i]
            arr[i] = arr[arr[i]]
            arr[temp] = temp
        else:
            i += 1

arr = [-1, -1, 6, 1, 9, 3, 2, -1, 4, -1]

modifyArr3(arr)
print(" ".join(map(str, arr)))










