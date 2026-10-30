class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        right = len(nums) - 1
        count = 0

        while left <= right:
            if nums[left] == val:
                while left <= right:
                    if nums[right] == val:
                        right -= 1
                    else:
                        temp = nums[left]
                        nums[left] = nums[right]
                        nums[right] = temp
                        right -= 1
                        break
            left += 1
        
        for i in nums:
            if i == val:
                break
            count += 1
        return count

