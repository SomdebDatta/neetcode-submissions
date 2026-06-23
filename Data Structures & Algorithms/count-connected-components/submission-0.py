class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if n <= 1:
            return n
        hashmap = {i: [] for i in range(n)}

        for x, y in edges:
            hashmap[x].append(y)
            hashmap[y].append(x)

        visited = set()
        self.connected = 0
        
        def dfs(curr, prev):
            if curr in visited:
                return
            if prev not in visited:
                self.connected += 1
            visited.add(curr)
            for neighbor in hashmap[curr]:
                if neighbor == prev:
                    continue
                dfs(neighbor, curr)
        
        for node in hashmap:
            dfs(node, -1)
        
        return self.connected
            