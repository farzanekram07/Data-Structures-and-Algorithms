## My own view to catch
## logic of smaller and greater to track




# Given an array of n integers, find the 3 elements 
# such that a[i] < a[j] < a[k] and i < j < k in 0(n) 
# time. If there are multiple such triplets, then 
# print any one of them.

# Examples:  
# Input: arr[] = {12, 11, 10, 5, 6, 2, 30}
# Output: 5, 6, 30
# Explanation: As 5 < 6 < 30, and they 
# appear in the same sequence in the array 



# brute force
def naive(arr):
    list = []
    for i in range(len(arr)):
        for j in range(i+ 1, len(arr)):
            for k in range(j + 1, len(arr)): 
                if arr[i] < arr[j] > arr[k] and i < j < k:
                    list.append([arr[i], arr[j], arr[k]])
    return list
                
arr = [3, 1, 5,  0, 4]
print(naive(arr))



# naive approach - O(N)|O(N)
def naive(arr):
    n = len(arr)
    max = n-1
    min = 0

    smaller = [0] * 10
    smaller[0] = -1
    for i in range(1, n):
        if arr[i] <= arr[min]:
            min = i
            smaller[i] = -1
        else:
            smaller[i] = min

    greater = [0]*10
    greater[n-1] = -1
    for i in range(n-2, -1, -1):
        if (arr[i] >= arr[max]):
            max = i
            greater[i] = -1
        else:
            greater[i] = max
            
    print("smaller: ", smaller)
    print("Greater: ", greater)
    # return smaller, greater


    for i in range(n):
        if smaller[i] != -1 and greater[i] != -1:
            print(arr[smaller[i]], arr[i], arr[greater[i]])
            return
        
    print("No triplet found!")
    return

arr = [1, 2, 3, 4, 5]
naive(arr)




## O(N)|O(1) using sys - pending




## what i see during solving the leetcode problem
from typing import List
class Solution:
    def increasingTriplet(nums : List[int]) -> bool:
        first = float('inf')
        second = float('inf')
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False
    
nums = [1, 2, 3, 4, 5]
print(Solution.increasingTriplet(nums))