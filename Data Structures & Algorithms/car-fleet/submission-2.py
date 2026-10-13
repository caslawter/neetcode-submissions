from typing import List
from math import ceil

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        cars = []
        sorted_cars = []
        ans = 0

        if len(position) == 0 or len(speed) == 0:
            return ans
        
        for index, pos in enumerate(position):
            car = {}
            car["position"] = pos
            car["speed"] = speed[index]
            cars.append(car)

        sorted_cars = sorted(cars, key=lambda x: x["position"])

        for index in range(len(sorted_cars), 0, -1):
            car = sorted_cars[index - 1]
            tth = (target - car["position"]) / car["speed"]

            if len(stack) == 0:
                stack.append(tth)
            elif stack[-1] < tth:
                stack.append(tth)
        return len(stack)