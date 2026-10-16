from math import floor

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        if len(nums) == 0:
            return -1

        left = 0
        right = len(nums)
        mid = floor((right + left) / 2)
        while left <= right:
            if mid >= len(nums):
                return -1
            
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                left = mid + 1
                mid = floor((right + left) / 2)
            else:
                right = mid - 1
                mid = floor((right + left) / 2)
        return -1
