class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set(nums)
        longest = []

        for num in hashSet:
            
            if num - 1 in hashSet:
                continue

            temp = [num]
            while True:

                if temp[-1] + 1 in hashSet:
                    temp.append(temp[-1] + 1)
                else:
                    break

            if len(temp) > len(longest):
                longest = temp

        return len(longest)