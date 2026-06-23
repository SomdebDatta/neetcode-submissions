class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {i: [] for i in range(n)}

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
                
                if not dfs(neighbor, curr):
                    return False
            return True
        
        return dfs(0, -1) and len(visited) == n