# 

def rotate(arr, k):
    return arr[k:] + arr[:k]

arr = [1, 2, 3, 4, 5]
k = 2
print(rotate(arr, k))
