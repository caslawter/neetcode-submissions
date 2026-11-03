class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.reverse()

        left1 = 0
        right1 = k % len(nums) - 1

        while left1 <= right1:
            temp = nums[left1]
            nums[left1] = nums[right1]
            nums[right1] = temp
            left1 += 1
            right1 -= 1

        left2 = k % len(nums)
        right2 = len(nums) - 1

        while left2 <= right2:
            temp = nums[left2]
            nums[left2] = nums[right2]
            nums[right2] = temp
            left2 += 1
            right2 -= 1