class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        elementMap = {}
        ans = []
        limit = 0
        for index,element in enumerate(nums):
            if element in elementMap:
                elementMap[element] = elementMap.get(element) + 1
            else:
                elementMap[element] = 1

        sortedElements = dict(sorted(elementMap.items(), key=lambda item:item[1], reverse= True))
        for key,element in sortedElements.items():
            if limit != k:
                ans.append(key)
                limit +=1
            else:
                break
        return ans