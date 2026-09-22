class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parents = [n for n in range(n)]
        rank = [1] * n
        components = 0

        def find_par(node):
            if node == parents[node]:
                return node
            
            parents[node] = find_par(parents[node])
            return parents[node]

        def union(x, y):
            par_x, par_y = find_par(x), find_par(y)

            if par_x == par_y:
                return 

            if rank[par_x] > rank[par_y]:
                parents[par_y] = parents[par_x]
                rank[par_x] += rank[par_y]
            else:
                parents[par_x] = parents[par_y]
                rank[par_y] += rank[par_x]

        for a, b in edges:
            union(a, b)
        
        for i in range(n):
            find_par(i)
        return len(set(parents))