class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for index, num in enumerate(nums):
            hashMap[num] = index

        for index, num in enumerate(nums):
            remainder = target - num
            if hashMap.get(remainder, None) is not None:
                index1 = hashMap.get(remainder)
                if index1 == index:
                    continue
                if index1 > index:
                    return [index, index1]
                else:
                    return [index1, index]
        