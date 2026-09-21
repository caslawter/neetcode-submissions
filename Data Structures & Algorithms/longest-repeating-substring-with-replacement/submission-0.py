class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashMap = {}
        left = 0
        right = 0
        longest = 0
        maxFreq = 0

        if len(s) == 0:
            return 0

        for right in range(len(s)):
            hashMap[s[right]] = hashMap.get(s[right], 0) + 1
            maxFreq = max(maxFreq,hashMap[s[right]] )

            while (right - left + 1) - maxFreq > k:
                hashMap[s[left]] -= 1
                left += 1

        longest = max(longest, right - left + 1)
        return longest   