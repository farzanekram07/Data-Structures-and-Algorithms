#1 Unique Pairs (unordered) - (1, 2), (1, 3), (2, 3)
def pairs(arr):
    # for i in arr:
    #     for j in arr:
    #         if i < j:
    #             print([i, j], end = " ")
    # print()
    return [[i,j] for i in arr for j in arr if i < j]

arr = [1, 2, 3]
unique_pairs = pairs(arr)
print(unique_pairs)


# Slight Optimization - Works even if arr has duplicate values

def pairs1(arr):
    return set(tuple(sorted((arr[i], arr[j]))) for i in range(len(arr)) for j in range(i+1, len(arr)))
arr = [6, 4, 8, 4]
print(pairs1(arr))