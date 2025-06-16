# iterative 

def linear_search(arr, k):
    for i in range(len(arr)):
        if arr[i] == k:
            return i
    return -1

arr = [10, 20, 30, 40, 50]
k = int(input("Enter the number you want to search: "))

result = linear_search(arr, k)
if result == -1:
    print("Element is not present in Array!")
else:
    print("Element is present in Array!")


