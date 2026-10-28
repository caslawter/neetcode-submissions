class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        ans = 0
        remainder = None

        while left <= right:
            print(remainder)
            mid = (left + right) // 2

            if mid * mid == x:
                return mid
            elif mid * mid > x:
                right = mid - 1
            elif mid * mid < x:
                currRemainder = x - (mid * mid)
                if remainder is None:
                    remainder = currRemainder
                    ans = mid
                if currRemainder > 0 and remainder > currRemainder:
                    remainder = currRemainder
                    ans = mid
                left = mid + 1

        return ans