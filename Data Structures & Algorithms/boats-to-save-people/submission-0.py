class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        left = 0
        right = len(people) - 1
        ans = 0

        while left <= right:
            if people[left] + people[right] <= limit:
                ans += 1
                left += 1
                right -= 1
            elif people[left] + people[right] > limit:
                ans += 1
                right -= 1
        return ans
