class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        left = 0
        right = len(nums2) - 1

        for index in range(len(nums1) - 1, -1, -1):

            if right < 0:
                break
            if nums1[index] == 0:
                nums1[index] = nums2[right]
                right -= 1

        nums1.sort()
