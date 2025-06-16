# iterative - O(N)|O(1)

def check(arr):
    n = len(arr)

    for i in range(n-1):
            if arr[i] < arr[i +1]:
                pass
            else:
                return False
    return True
        
arr = [10, 20, 30, 40]
res = check(arr)
if res == True:
    print("Array is sorted!")
else:
    print("Array is unsorted!")


# make for readable code + oops concept

class array_checker:
    def __init__(self, arr):
        self.arr = arr

    def is_sorted_ascending(self):
        for i in range(len(self.arr)-1):
            if self.arr[i] > arr[i+1]:
                return False
        return True

    def is_sorted_descending(self):
        for i in range(len(self.arr)-1):
            if self.arr[i] < arr[i+1]:
                return False
        return True

    def checker(self):
        return self.is_sorted_ascending() or self.is_sorted_descending()


arr = [10, 20, 80, 40]
res = array_checker(arr)
if res.checker == True:
    print("Array is sorted!")
else:
    print("Array is unsorted!")
  

# Showcasing Object-Oriented Programming (OOP) principles:
# Encapsulation: The sorting checks are encapsulated in 
# their own functions.
# Modularity: Each function has a single responsibility.