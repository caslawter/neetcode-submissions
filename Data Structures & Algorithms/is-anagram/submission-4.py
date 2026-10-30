class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        freq = [0] * 26

        for char in s:
            freq[ord(char) - ord('a')] += 1
        
        key1 = tuple(freq)
        freq = [0] * 26
        for char in t:
            freq[ord(char) - ord('a')] += 1


        key2 = tuple(freq)

        if key1 == key2:
            return True
        else:
            return False