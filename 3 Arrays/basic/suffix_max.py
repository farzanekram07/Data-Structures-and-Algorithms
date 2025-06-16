# iterative - O(N)|O(N)

def suffix_maximum(arr):
    n = len(arr)
    suffix_max = [0] * n
    suffix_max[n-1] = arr[-1]

    for i in range(n-2, -1, -1):
        suffix_max[i] = max(arr[i], suffix_max[i+1])


    return suffix_max

arr = [4, 2, 8, 5, 6, 3]
print(suffix_maximum(arr))