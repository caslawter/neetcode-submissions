class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        left = 0
        right = 0
        length = len(word1) + len(word2)
        count = 0
        ans = ""
        while count <= length:

            if left >= len(word1):
                ans += word2[right:]
                break
            elif right >= len(word2):
                ans += word1[left:]
                break

            if count % 2 == 0:
                ans += word1[left]
                left += 1
            elif count % 2 == 1:
                ans += word2[right]
                right += 1

            count += 1
        return ans