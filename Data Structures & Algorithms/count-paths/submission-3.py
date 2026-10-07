class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = {}
        
        def backtracking(x, y):
            if x not in range(m) or y not in range(n):
                return 0
            
            if x == m - 1 and y == n - 1:
                return 1
            
            if (x, y) in cache:
                return cache[(x, y)]
            
            cache[(x, y)] = backtracking(x + 1, y) + backtracking(x, y + 1)
            return cache[(x, y)]
        
        return backtracking(0, 0)
