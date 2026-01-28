# iterative approach
def removeZeroes(arr):
    res = []
    for i in range(len(arr)):
        if arr[i] != 0:
            res.append(arr[i])
    return res

def inPlace(arr):
    j = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[j] = arr[i]
            j += 1
    return j


if __name__ == "__main__":
    array = list(map(int, input("Enter the numbers: ").split()))
    print(removeZeroes(array))

    array = list(map(int, input("Enter the numbers: ").split()))
    res = inPlace(array)
    print(array[:res])
