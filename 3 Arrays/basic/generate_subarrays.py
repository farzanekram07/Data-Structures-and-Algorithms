# iterative - O(N3)|O(1)

def generate(arr):
    n = len(arr)

    for i in range(n):
        for j in range(i, n):
            for k in range(i, j+1):
                print(arr[k], end = " ")
            print()

arr = [1, 2, 3]
generate(arr)


# iterative - O(N2)|O(1)

def generative(arr):
    n = len(arr)

    for i in range(n):
        for j in range(i, n):
            print(arr[i:j+1], end = "\n")

arr = [1, 2, 3]
generative(arr)

            
