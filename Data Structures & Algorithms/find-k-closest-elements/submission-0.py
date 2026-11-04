from collections import deque

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        queue = deque()


        for element in arr:
            if len(queue) < k:
                queue.append(element)
            elif abs(element - x) < abs(queue[0] - x):
                queue.popleft()
                queue.append(element)

        return list(queue)
