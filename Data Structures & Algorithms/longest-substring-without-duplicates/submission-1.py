class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        hashSet = set()
        longest = 0

        while right < len(s):
            if s[right] not in hashSet:
                hashSet.add(s[right])
                right += 1
            else:
                hashSet.remove(s[left])
                left += 1

            if len(hashSet) > longest:
                longest = len(hashSet)

        return longest