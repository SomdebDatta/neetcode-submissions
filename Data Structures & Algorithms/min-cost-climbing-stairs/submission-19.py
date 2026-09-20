class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = [-1] * (len(cost))
        
        def recursion(idx):
            if idx >= len(cost):
                return 0
            
            if cache[idx] != -1:
                return cache[idx]

            cache[idx] = cost[idx] + min(
                recursion(idx + 1),
                recursion(idx + 2)
            )

            return cache[idx]
        
        return min(recursion(0), recursion(1))


