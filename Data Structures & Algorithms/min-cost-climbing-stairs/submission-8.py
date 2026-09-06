class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        ans = [0] * (len(cost) + 1)
        ans[0] = cost[0]
        ans[1] = cost[1]

        for i in range(2, len(cost)):
            ans[i] = cost[i] + min(ans[i - 1], ans[i - 2])
        
        return ans[len(cost) - 1]





        cost.append(0)
        cache = [-1] * (len(cost) + 1)
        
        def recursion(curr):
            if curr == 0 or curr == 1:
                return cost[curr]
            
            if cache[curr] != -1:
                return cache[curr]
            
            cache[curr] = cost[curr] + min(recursion(curr - 1), recursion(curr - 2))
            return cache[curr]
        
        return recursion(len(cost) - 1)
        
