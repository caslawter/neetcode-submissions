class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0:
            return 0
        left = 0
        right = len(height) - 1
        maxLeft = height[0]
        maxRight = height[-1]
        maxArea = 0

        while left <= right:
            if maxRight > maxLeft:
                area = maxLeft - height[left]
                if area > 0:
                    maxArea += area
                maxLeft = max(maxLeft, height[left])
                left+=1
            else:
                area = maxRight - height[right]
                if area > 0:
                    maxArea += area
                maxRight= max(maxRight, height[right])
                right -= 1
        return maxArea
                        