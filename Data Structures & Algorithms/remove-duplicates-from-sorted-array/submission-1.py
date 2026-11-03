class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = set()

        left = 0
        right = 0

        while left <= len(nums) - 1:
            if nums[left] not in seen:
                seen.add(nums[left])
            else:
                while right <= len(nums) - 1:
                    if nums[right] not in seen:
                        seen.add(nums[right])
                        nums[left] = nums[right]
                        break
                    else:
                        right += 1
            left += 1
            right += 1
        return len(seen)