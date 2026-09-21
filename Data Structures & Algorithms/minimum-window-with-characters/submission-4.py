class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        bestLeft = 0
        bestRight = -1
        left = 0
        right = 0
        shortest = ""

        freqMap = {}
        tempMap = {}
        matches = 0

        for char in t:
            freqMap[char] = freqMap.get(char, 0) + 1

        while right < len(s):
            if s[right] in freqMap:
                tempMap[s[right]] = tempMap.get(s[right], 0) + 1
                if tempMap.get(s[right]) == freqMap.get(s[right]):
                    matches += 1
                
            if matches == len(freqMap):
                if bestRight == -1 or (right - left) + 1 < (bestRight - bestLeft + 1):
                    bestLeft, bestRight = left, right
                
                while left <= right and left <= len(s):
                    if s[left] in freqMap:
                        if tempMap.get(s[left]) - 1 >= freqMap.get(s[left]):
                            tempMap[s[left]] = tempMap.get(s[left]) - 1
                            left+=1
                            if bestRight == -1 or (right - left) + 1 < (bestRight - bestLeft + 1):
                                bestLeft, bestRight = left, right
                            
                        else:
                            break
                    else:
                        left += 1
                        if bestRight == -1 or (right - left) + 1 < (bestRight - bestLeft + 1):
                            bestLeft, bestRight = left, right
                        
            right += 1
        return s[bestLeft:bestRight+1] if bestRight != -1 else ""
            
