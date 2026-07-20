class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combined_list = []

        for i in range(len(position)):
            time = (target - position[i]) / speed[i]
            combined_list.append([position[i], speed[i], time])
        
        combined_list.sort(key=lambda x: x[0], reverse=True)
        
        ans = 0
        curr_max = float('-inf')

        for position, speed, time in combined_list:
            if time > curr_max:
                ans += 1
                curr_max = time
        
        return ans