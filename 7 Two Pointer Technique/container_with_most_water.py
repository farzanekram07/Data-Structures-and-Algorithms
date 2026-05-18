class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        width = right - left 
        maximumArea = min(height[left], height[right]) * width

        while left < right:
            width = right - left
            currentArea = min(height[left], height[right]) * width
            maximumArea = max(currentArea, maximumArea)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return maximumArea

height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))
