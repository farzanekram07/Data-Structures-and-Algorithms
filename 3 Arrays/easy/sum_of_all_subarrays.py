# brute force - O(N3)|O(1)
def sum_subarrays(arr):
    n = len(arr)
    sum = 0
    for i in range(n):
        for j in range(i, n):
            for k in range(i, j+1):
                sum += arr[k]
    return sum 
                
arr = [1, 2, 3]
print(sum_subarrays(arr))


# naive approach - O(N2)|O(1)
def sum_of_subarrays(arr):
    n = len(arr)
    res = 0
    sumSubarrays_sums = []

    for i in range(n):
        temp = 0
        for j in range(i, n):
            temp += arr[j]
            res += temp
            sumSubarrays_sums.append(temp)
    return res, sumSubarrays_sums

arr = [1, 2, 3]
print(sum_of_subarrays(arr))


# expected appraoch - O(N)|O(1)
def sumSubarrays(arr):
    n = len(arr)
    res = 0

    for i in range(n):
        res += arr[i] * (i+1) * (n-i)
    return res

arr = [1, 2, 3]
print(sumSubarrays(arr))



