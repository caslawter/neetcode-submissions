class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0

        while fast <= len(nums) - 1 or slow <= len(nums) -1:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if nums[slow] == nums[fast]:
                slow2 = 0
                while True:
                    if slow == slow2:
                        return slow
                    else:
                        slow = nums[slow]
                        slow2 = nums[slow2]
        