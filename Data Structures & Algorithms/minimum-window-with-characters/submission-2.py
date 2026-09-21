class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

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
                if shortest == "" or len(s[left:right+1]) < len(shortest):
                    shortest = s[left:right+1]
                
                while left <= right and left <= len(s):
                    if s[left] in freqMap:
                        if tempMap.get(s[left]) - 1 >= freqMap.get(s[left]):
                            tempMap[s[left]] = tempMap.get(s[left]) - 1
                            left+=1
                            if shortest == "" or len(s[left:right+1]) < len(shortest):
                                shortest = s[left:right+1]
                            
                        else:
                            break
                    else:
                        left += 1
                        if shortest == "" or len(s[left:right+1]) < len(shortest):
                            shortest = s[left:right+1]
                        
            right += 1
        return shortest

            
