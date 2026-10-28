class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashMap = {}

        for index, num in enumerate(nums):
            if hashMap.get(num, None) is None:
                hashMap[num] = [index]
            else:
                arr = hashMap.get(num)
                if abs(arr[-1] - index) <= k:
                    return True
                else:
                    arr.append(index)
        return False
