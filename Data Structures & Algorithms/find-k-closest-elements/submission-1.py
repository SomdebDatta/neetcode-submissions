class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        minHeap = []
        heapq.heapify(minHeap)

        for num in arr:
            heapq.heappush(minHeap, [abs(x - num), num])
        
        ans = []

        for i in range(k):
            ans.append(heapq.heappop(minHeap)[1])

        return sorted(ans)