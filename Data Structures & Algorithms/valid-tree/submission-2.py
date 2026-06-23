class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
            
        preMap = {i: [] for i in range(n)}

        for e1, e2 in edges:
            preMap[e1].append(e2)
            preMap[e2].append(e1)
        
        visited = set()
        
        def dfs(curr, prev):
            if curr in visited:
                return False
            
            visited.add(curr)

            for edge in preMap[curr]:
                if edge == prev:
                    continue
                if not dfs(edge, curr): return False

            return True
        
        return dfs(0, -1) and len(visited) == n