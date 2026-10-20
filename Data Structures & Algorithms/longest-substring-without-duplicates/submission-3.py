class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashSet = set()
        left = 0
        right = 0
        longest = 0

        while right <= len(s) - 1:
            if s[right] not in hashSet:
                hashSet.add(s[right])
                longest = max(longest, len(hashSet))
                right += 1
            else:
                hashSet.remove(s[left])
                left += 1

        return longest