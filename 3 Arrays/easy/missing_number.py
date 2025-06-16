
# brute force
def missing_number(arr):
    for i in range(1,len(arr)+1):
        if i not in arr:
            return i
        
arr = [1, 2, 4, 5]
print(missing_number(arr))



# formula
def missing_number(arr):
    return sum(arr) == len(arr) * (len(arr)+1)//2

arr = [1, 2, 3]
print(missing_number(arr))



# using hashtable of list
def missingNum(arr):
    n = max(arr)
    hashtable = [0] * (n + 1)

    for num in arr:
        hashtable[num] += 1
    print(hashtable)

    list = []
    for i in range(1, n+1):
        if hashtable[i] == 0:
            list.append(i)
    return list

arr = [1, 2, 9]
print(missingNum(arr))