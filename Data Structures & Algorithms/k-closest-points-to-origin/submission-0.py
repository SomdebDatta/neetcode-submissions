class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        min_heap = []
        ans = []
        
        for idx, (x, y) in enumerate(points):
            dist = x ** 2 + y ** 2
            heapq.heappush(min_heap, (dist, idx))
        
        for _ in range(k):
            dist, idx = heapq.heappop(min_heap)
            ans.append(points[idx])
        
        return ans