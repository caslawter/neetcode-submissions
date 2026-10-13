from typing import List

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet_count = -1
        last_speed = 0
        cars = []

        if len(position) == 0 or len(speed) == 0:
            return 0

        cars = sorted(zip(position, speed))

        for index in range(len(cars), 0, -1):
            car = cars[index - 1]
            tth = (target - car[0]) / car[1]

            if fleet_count == -1:
                last_speed = tth
                fleet_count = 1
            elif tth > last_speed:
                last_speed = tth
                fleet_count += 1
        return fleet_count