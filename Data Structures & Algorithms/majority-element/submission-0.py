class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cur = None
        curCount = 0

        for num in nums:
            if cur is None:
                cur = num
                curCount += 1
            elif cur == num:
                curCount += 1
            elif cur != num:
                if curCount == 0:
                    cur = num
                    curCount += 1
                else:
                    curCount -= 1
        return cur