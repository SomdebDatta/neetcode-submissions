class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:        
        if n == 1:
            return n

        ans = 0
        adj = {i:[] for i in range(n)}

        for edge1, edge2 in edges:
            adj[edge1].append(edge2)
            adj[edge2].append(edge1)
        
        visited = set()

        def dfs(curr, prev):
            if curr in visited:
                return False
            
            visited.add(curr)
            for neighbor in adj[curr]:
                if neighbor == prev:
                    continue
                dfs(neighbor, curr)
            return True
        
        for i in range(n):
            if dfs(i, -1):
                ans += 1
        
        return ans
            