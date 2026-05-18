def twoSumII(arr, target):
    left = 0
    right = len(arr)-1

    while left < right:
        if arr[left] + arr[right] < target:
            left += 1
        elif arr[left] + arr[right] > target:
            right -= 1
        elif arr[left] + arr[right] == target:
            return [left+1, right+1]  # 1-indexed

numbers = [1,2,3,4]
target = 3
print(twoSumII(numbers, target)) 
