class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        ans = 0

        while left <= right:
            mid = (left + right) // 2
            minDays = 1
            totalWeight = 0

            for weight in weights:
                if totalWeight + weight <= mid:
                    totalWeight += weight
                else:
                    minDays += 1
                    totalWeight = weight

                if minDays > days:
                    left = mid + 1
                    break
            
            if minDays <= days:
                if ans == 0:
                    ans = mid
                elif ans > mid:
                    ans = mid
                    
                right = mid - 1
        return ans