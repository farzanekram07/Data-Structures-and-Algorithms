# brute force - O(n*k)|O(1)

def duplicate(arr, k):
    n = len(arr)
    
    for i in range(n):
        for c in range(1, k + 1):
            j = i + c

            if j < n and arr[i] == arr[j]:
                return True
    return False
        
arr = [1, 2, 3, 1, 2, 3]
k = 2
print(duplicate(arr, k))



# hashing - O(N)|O(K)

def check_duplicate_within_k(arr, n, k):
    my_set = set()

    for i in range(n):
        if arr[i] in my_set:
            return True
        
        my_set.add(arr[i])

        if i >= k:
            my_set.remove(arr[i-k])
    return False

arr = [1, 2, 3, 4, 2, 3]
n = len(arr)
k = 3
print(check_duplicate_within_k(arr, n, k))         
