class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        count = 0

        while count < 2:
            count += 1
            for num in nums:
                ans.append(num)
        return ans