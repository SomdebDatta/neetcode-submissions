class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        
        adj = {i: [] for i in range(n)}

        for node1, node2 in edges:
            adj[node1].append(node2)
            adj[node2].append(node1)

        visited = set()
        
        def dfs(node, prevNode):
            if node in visited:
                return False
            
            visited.add(node)

            for child in adj[node]:
                if child == prevNode:
                    continue
                if not dfs(child, node):
                    return False
            return True
        
        return dfs(0, -1) and len(visited) == n