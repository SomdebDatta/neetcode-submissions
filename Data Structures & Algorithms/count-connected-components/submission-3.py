class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        rank = [1] * n
        parent = [node for node in range(n)]
        
        def findPar(node):
            if node == parent[node]:
                return node
            parent[node] = findPar(parent[node])
            return parent[node]
        
        def union(x, y):
            par_x, par_y = findPar(x), findPar(y)
            if par_x == par_y:
                return
            
            if rank[par_x] >= rank[par_y]:
                parent[par_y] = parent[par_x]
                rank[par_x] += rank[par_y]
            else:
                parent[par_x] = parent[par_y]
                rank[par_y] += rank[par_x]
        
        for a, b in edges:
            union(a, b)
        
        for i in range(n):
            findPar(i)
        
        return len(set(parent))