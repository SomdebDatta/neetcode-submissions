class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        path = []
        visited, cycle = set(), set()

        adjList = defaultdict(list)

        for crs, pre in prerequisites:
            adjList[crs].append(pre)
        
        def dfs(crs):
            if crs in cycle:
                return False
            
            if adjList[crs] is None:
                return True
            
            cycle.add(crs)
            for pre in adjList[crs]:
                if not dfs(pre): return False
            cycle.remove(crs)
            adjList[crs] = None
            path.append(crs)
            return True
        
        for i in range(numCourses):
            if not dfs(i): return []
        
        return path