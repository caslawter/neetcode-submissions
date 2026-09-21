class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        size = len(s1) - 1
        left = 0
        right = 0
        freqMap = {}
        tempMap = {}
        isValid = False
        for char in s1:
            freqMap[char] = freqMap.get(char, 0) + 1

        while right < len(s2) or left < len(s2):

            if right < len(s2):
                tempMap[s2[right]] = tempMap.get(s2[right], 0) + 1

            if tempMap == freqMap:
                isValid = True
                break

            if right - left >= size:
                left += 1
                tempMap[s2[left - 1]] = tempMap.get(s2[left - 1]) - 1
            elif right > len(s2) - 1:
                left += 1
                tempMap[s2[left - 1]] = tempMap.get(s2[left - 1]) - 1

            if tempMap.get(s2[left - 1]) == 0:
                del tempMap[s2[left - 1]]

            if right <= len(s2) - 1:
                right += 1

        return isValid
    