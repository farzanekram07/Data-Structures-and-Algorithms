# iterative approach

def print_alternatives(list):
    for i in range(len(list)):
        if i % 2 == 0:
            print(list[i], end = " ")
    print()

list = [10, 20, 30, 40, 50]
print_alternatives(list)


def alternatives(arr):
    res = []

    for i in range(0, len(arr), 2):
        res.append(arr[i])
    return res

arr = [10, 20, 30, 40, 50]
print("list return", alternatives(arr))

res = alternatives(arr)
print(" ".join(map(str, res)))



# recursive approach 

def getAlternatesRec(arr, idx, res):
    if idx < len(arr):
        res.append(arr[idx])
        getAlternatesRec(arr, idx + 2, res)

def getAlternates(arr):
    res = []
    getAlternatesRec(arr, 0, res)
    return res

if __name__ == "__main__":
    arr = [10, 20, 30, 40, 50]
    res = getAlternates(arr)
    print(" ".join(map(str, res)))
