"""
Car fleet: https://leetcode.com/problems/car-fleet/
"""
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if len(position) == 1:
            return 1

        cars = [[d, v] for d, v in zip(position, speed)]
        cars.sort(key=lambda d:d[0], reverse=True)
        fleets = prev_time = 0

        for d, v in cars:
            dest_time = (target - d) / v

            if dest_time > prev_time:
                fleets += 1
                prev_time = dest_time

        return fleets

        
        
