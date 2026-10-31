class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        preFixArr = []
        postFixArr = [0] * len(nums)
        ans = []
        prefix = 1
        postfix = 1
        for i in nums:
            preFixArr.append(prefix)
            prefix *= i
            
        
        for i in range(len(nums) - 1, -1,-1):
            postFixArr[i] = postfix
            postfix *= nums[i]

        for index, num in enumerate(nums):
            total = preFixArr[index] * postFixArr[index]
            ans.append(total)

        return ans