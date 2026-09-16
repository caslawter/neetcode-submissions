class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ans = []
        hashMap = {}
        found = False
        for index,value in enumerate(numbers):
            if value in hashMap:
                temp = hashMap.get(value)
                temp.append(index)
                hashMap[value] = temp
            else:
                hashMap[value] = [index]

        for index, number in enumerate(numbers):
            if not found:
                remainder = target - number
                if remainder in hashMap:
                    arr = hashMap[remainder]
                    for j in arr:
                        if j != index:
                            found = True
                            ans.append(index + 1)
                            ans.append(j + 1)
                            break
            else:
                break
        return ans