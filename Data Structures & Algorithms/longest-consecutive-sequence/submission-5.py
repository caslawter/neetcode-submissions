class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set(nums)
        ans = []
        longest = []


        for i in hashSet:
            if i - 1 not in hashSet:
                ans = [i]
            while True:
                if len(ans) == 0:
                    ans.append(i)
                elif ans[-1] + 1 in hashSet:
                    ans.append(ans[-1] + 1)
                else:
                    break
            if len(ans) > len(longest):
                longest = ans
        return len(longest)