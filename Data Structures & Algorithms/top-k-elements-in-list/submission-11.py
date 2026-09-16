class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        elementMap = {}
        ans = []
        bucket = [None] * (len(nums) + 1)
        limit = 0
        for element in nums:
            if element in elementMap:
                elementMap[element] = elementMap.get(element) + 1
            else:
                elementMap[element] = 1

        for key, value in elementMap.items():
            if bucket[value] == None:
                bucket[value] = [key]
            else:
                bucket[value].append(key)
                
        bucket.reverse()
        for i in bucket:
            if limit == k:
                break
            else:
                if i != None:
                    for j in range(len(i) - 1, -1 ,-1):
                        print(j)
                        if limit == k:
                            break
                        else:
                            ans.append(i[j])
                            limit += 1   
        return ans