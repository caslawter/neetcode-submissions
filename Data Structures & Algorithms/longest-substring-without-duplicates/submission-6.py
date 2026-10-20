class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashSet = {}
        left = 0
        right = 0
        longest = 0

        while right <= len(s) - 1:
            if s[right] in hashSet and hashSet[s[right]] >= left:
                left = hashSet[s[right]] + 1

            hashSet[s[right]] = right
            longest = max(longest, right - left + 1)
            right += 1

        return longest