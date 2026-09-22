class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parents = [n for n in range(len(edges))]
        rank = [1] * len(edges)

        def find_par(node):
            print(node)
            if parents[node] == node:
                return node
            parents[node] = find_par(parents[node])
            return parents[node]
        

        def union(x, y):
            par_x, par_y = find_par(x), find_par(y)

            if par_x == par_y:
                return True
            
            if rank[par_x] > rank[par_y]:
                parents[par_y] = parents[par_x]
                rank[par_x] += rank[par_y]
            else:
                parents[par_x] = parents[par_y]
                rank[par_y] += rank[par_x]

            return False
        

        for a, b in edges:
            if union(a - 1, b - 1):
                ans = [a, b]
        
        return ans