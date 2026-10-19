class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        wordMap = {}
        ans = []        
        for word in strs:
            count = [0] * 52
            
            for char in word:
                count[ord(char) - ord('a')] += 1

            key = tuple(count)

            if key in wordMap:
                arr = wordMap.get(key)
                arr.append(word)
                wordMap[key] = arr
            else:
                wordMap[key] = [word]

        for key,value in wordMap.items():
            ans.append(value)
        return ans
