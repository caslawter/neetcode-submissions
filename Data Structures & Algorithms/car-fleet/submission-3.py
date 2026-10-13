from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet_count = 0
        last_speed = 0
        cars = []
        sorted_cars = []
        ans = 0

        if len(position) == 0 or len(speed) == 0:
            return ans

        cars = list(zip(tuple(position), tuple(speed)))

        sorted_cars = sorted(cars, key=lambda x: x[0])

        for index in range(len(sorted_cars), 0, -1):
            car = sorted_cars[index - 1]
            tth = (target - car[0]) / car[1]

            if fleet_count == 0:
                last_speed = tth
                fleet_count+=1
            elif tth > last_speed:
                last_speed = tth
                fleet_count += 1
        return fleet_count