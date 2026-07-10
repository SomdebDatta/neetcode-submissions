class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = defaultdict(list)

        for crs, pre in prerequisites:
            adjList[crs].append(pre)
        
        seen = set()

        def dfs(crs):
            if crs in seen:
                return False
            
            if adjList[crs] == []:
                return True
            
            seen.add(crs)
            for pre in adjList[crs]:
                if not dfs(pre): return False
            seen.remove(crs)
            adjList[crs] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True