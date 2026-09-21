class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combined = []

        for pos, spd in zip(position, speed):
            combined.append([pos, spd])
        
        combined.sort(key=lambda x:x[0])

        # print(combined)
        fleet = 0

        while combined:
            fleet += 1
            pos, spd = combined.pop()
            while combined and (target - combined[-1][0]) / combined[-1][1] <= (target - pos) / spd:
                combined.pop()
        
        return fleet