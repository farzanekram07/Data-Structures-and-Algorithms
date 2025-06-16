def binarySearch(nums, target):
    nums.sort()
    low = 0
    high =  len(nums)
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            low = mid + 1 
        else:
            high = mid -1 
        
    return -1

key = int(input())
nums = [3, 1, 5, 2, 4, 8, 7]
print(binarySearch(nums, key))
