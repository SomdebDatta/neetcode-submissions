class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = [-1] * (len(cost))

        def recursion(curr):
            if curr == 0 or curr == 1:
                return cost[curr]
            if cache[curr] != -1:
                return cache[curr]

            cache[curr] = cost[curr] + min(recursion(curr - 1), recursion(curr - 2))
            return cache[curr]
        
        return min(recursion(len(cost) - 1), recursion(len(cost) - 2))