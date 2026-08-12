class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parents = [n for n in range(len(edges))]
        rank = [0] * len(edges)

        def findPar(x):
            if x == parents[x]:
                return x
            parents[x] = findPar(parents[x])
            return parents[x]
        
        def union(x, y):
            x_par = findPar(x)
            y_par = findPar(y)
            if x_par == y_par:
                return True
            
            if rank[x_par] >= rank[y_par]:
                parents[y_par] = x_par
                rank[x_par] += rank[y_par]
            else:
                parents[x_par] = y_par
                rank[y_par] += rank[x_par]
            
            return False

        ans = []
        for a, b in edges:
            if union(a - 1, b - 1):
                ans = [a, b]
        
        return ans
