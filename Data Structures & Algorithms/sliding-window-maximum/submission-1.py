from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        ans = []
        for index, num in enumerate(nums):

            if queue and queue[0] <= index - k:
                queue.popleft()

            while queue and num > nums[queue[-1]]:
                queue.pop()
            queue.append(index)

            if index >= k - 1:
                ans.append(nums[queue[0]])
            
        return ans