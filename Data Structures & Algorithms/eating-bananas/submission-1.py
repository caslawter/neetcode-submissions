from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        left = 1
        right = max(piles)
        ans = 0

        while left <= right:
            mid = (left + right) // 2

            totalHour = 0
            for pile in piles:
                totalHour += self.getHours(pile, mid)

            if totalHour <= h:
                if ans == 0:
                    ans = mid
                elif ans > mid:
                    ans = mid
                right = mid - 1
            elif totalHour >= h:
                left = mid + 1

        return ans
    def getHours(self, pile, speed):
        return ceil(pile / speed)