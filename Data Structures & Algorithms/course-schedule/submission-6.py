class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = defaultdict(list)

        for a, b in prerequisites:
            adj_list[a].append(b)
        
        seen = set()
        
        def dfs(node):
            if adj_list[node] == []:
                return True

            if node in seen:
                return False
            
            seen.add(node)
            
            for pre in adj_list[node]:
                if not dfs(pre):
                    return False
            adj_list[node] = []
            # seen.remove(node)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True
