def maxSubArray(arr):
        maxSum = arr[0]
        currentSum = arr[0]
        for i in range(1, len(arr)):
            currentSum = max(currentSum + arr[i], arr[i])
            maxSum = max(currentSum, maxSum)
        return maxSum

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))
