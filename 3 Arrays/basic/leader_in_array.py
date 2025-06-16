# Given an array arr[] of size n, the task is to find 
# all the Leaders in the array. An element is a Leader 
# if it is greater than or equal to all the elements to 
# its right side.
# Note: The rightmost element is always a leader.

# iterative - O(N2)|O(N)

def leader_in_array(arr):
    n = len(arr)
    leaders = []

    for i in range(n):
        leader = arr[i]
        if all(leader > arr[j] for j in range(i+1 ,n)):
            leaders.append(leader)
    return leaders
        
arr = [16, 17, 4, 3, 5, 2]
print(leader_in_array(arr))


# iterative - O(N2)|O(N)

def leaders(arr):
    n = len(arr)
    result = []

    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] < arr[j]:
                break
        else:
            result.append(arr[i])

    return result

arr = [16, 17, 4, 3, 5, 2]
result = leaders(arr)
print(" ".join(map(str, result)))


# using suffix Maximum - O(N)|O(1)

def leader_in_the_array(arr):
    n = len(arr)
    result = []

    max = arr[-1]
    result.append(max)

    for i in range(n-2, -1, -1):
        if arr[i] >= max:
            max = arr[i]
            result.append(max)

    result.reverse()
    return result

arr = [16, 17, 4, 3, 5, 2]
result = leaders(arr)
print(result)

