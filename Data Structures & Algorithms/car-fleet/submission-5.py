class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = []

        for pos, spd in zip(position, speed):
            pos_speed.append([pos, spd])
        
        pos_speed.sort(key=lambda x:x[0])

        time = []

        for pos, spd in pos_speed:
            curr = (target - pos) / spd
            # print(curr)
            while time and time[-1] <= curr:
                time.pop()
            time.append(curr)
        
        return len(time)

