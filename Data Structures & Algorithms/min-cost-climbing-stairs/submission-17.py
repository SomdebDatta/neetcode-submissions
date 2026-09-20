class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cache = [-1] * (len(cost))
        
        def recursion(idx, curr):
            if idx >= len(cost):
                return 0
            
            if cache[idx] != -1:
                return cache[idx]

            cache[idx] = cost[idx] + min(
                recursion(idx + 1, curr),
                recursion(idx + 2, curr)
            )

            return cache[idx]
            # return min(
            #     recursion(idx + 1, curr + cost[idx]),
            #     recursion(idx + 2, curr + cost[idx])
            # )
        
        return min(recursion(0, 0), recursion(1, 0))
        
        # return min(recursion(0, 0), recursion(1, 0))


