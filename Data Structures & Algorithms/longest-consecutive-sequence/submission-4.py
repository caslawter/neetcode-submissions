import copy
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set(nums)
        orderedList = list(hashSet)
        orderedList.sort()
        ans = []
        longest = []
        for i in orderedList:
            
            if len(ans) == 0:
                ans.append(i)
                if len(ans) >= len(longest):
                    longest = ans
            elif ans[-1] + 1 == i:
                ans.append(i)
                if len(ans) >= len(longest):
                    longest = ans
            else:
                ans = [i]

        return len(longest)