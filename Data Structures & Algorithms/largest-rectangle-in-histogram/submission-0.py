class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []

        if len(heights) == 0:
            return 0

        for index, height in enumerate(heights):
            if len(stack) == 0:
                stack.append((index, height))
            elif stack[-1][1] > height:
                pair = ()
                while len(stack) != 0 and stack[-1][1] > height :
                    maxArea = max(maxArea, stack[-1][1] * (index - stack[-1][0]))
                    pair = stack.pop()
                
                stack.append((pair[0], height))
            else:
                stack.append((index, height))

        width = len(heights)
        for pair in stack:
            maxArea = max(maxArea, pair[1] * (width - pair[0]))
                
        return maxArea
