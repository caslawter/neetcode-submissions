class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for index, num in enumerate(numbers):
            remainder = target - num

            left = 0
            right = len(numbers) - 1
            mid = 0

            while left <= right:
                mid = (left + right) // 2
                if numbers[mid] == remainder:
                    if index != mid:
                        return [index + 1, mid + 1]
                    elif numbers[mid + 1] == remainder:
                        return [index + 1, mid + 2]
                    else:
                        break
                elif remainder > numbers[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
