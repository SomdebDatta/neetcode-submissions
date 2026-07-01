class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        def solveRecursion(pos):
            if pos >= len(days):
                return 0
            
            option1 = costs[0] + solveRecursion(pos + 1)

            idx = pos

            while idx < len(days) and days[idx] < days[pos] + 7:
                idx += 1

            option2 = costs[1] + solveRecursion(idx)
        
            idx = pos
            while idx < len(days) and days[idx] < days[pos] + 30:
                idx += 1
            
            option3 = costs[2] + solveRecursion(idx)

            return min(option1, option2, option3)
        

        def solveMem(pos):
            if pos >= len(days):
                return 0

            if dp[pos] != -1:
                return dp[pos]
            
            option1 = costs[0] + solveMem(pos + 1)

            idx = pos
            while idx < len(days) and days[idx] < days[pos] + 7:
                idx += 1
            option2 = costs[1] + solveMem(idx)

            idx = pos
            while idx < len(days) and days[idx] < days[pos] + 30:
                idx += 1
            option3 = costs[2] + solveMem(idx)
            
            dp[pos] = min(option1, option2, option3)

            return dp[pos]


        # return solveRecursion(0)

        dp = [-1] * (len(days) + 1)
        return solveMem(0)