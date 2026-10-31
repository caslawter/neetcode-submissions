class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        prefix = 1
        postfix = 1

        for i in range(len(nums) - 1, -1,-1):
            ans[i] = prefix
            prefix *= nums[i]
        for index, num in enumerate(nums):
            ans[index] = ans[index] * postfix
            postfix *= num

        return ans