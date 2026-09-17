class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        maxVol = 0

        while left < right:
            maxVol = max(min(heights[left], heights[right]) * (right - left), maxVol)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1 

        return maxVol