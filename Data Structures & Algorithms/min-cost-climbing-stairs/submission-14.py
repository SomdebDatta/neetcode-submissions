class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        ans = [0] * len(cost)

        ans[0] = cost[0]
        ans[1] = cost[1]

        for i in range(2, len(cost)):
            ans[i] = cost[i] + min(ans[i - 1], ans[i - 2])
        
        return min(ans[len(cost) - 1], ans[len(cost) - 2])



        cache = [-1] * len(cost)

        def recursion(curr):
            if curr == 0 or curr == 1:
                return cost[curr]
            if cache[curr] != -1:
                return cache[curr]

            cache[curr] = cost[curr] + min(recursion(curr - 1), recursion(curr - 2))
            return cache[curr]
        
        return min(recursion(len(cost) - 1), recursion(len(cost) - 2))