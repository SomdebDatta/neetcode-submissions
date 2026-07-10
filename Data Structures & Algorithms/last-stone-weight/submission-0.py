class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = [-stone for stone in stones]
        heapq.heapify(maxHeap)
        
        while len(maxHeap) > 1:
            stone1, stone2 = -(heapq.heappop(maxHeap)), -(heapq.heappop(maxHeap))
            if stone1 == stone2:
                continue
            heapq.heappush(maxHeap, -(abs(stone1 - stone2)))
        
        if len(maxHeap) == 0:
            return 0
        return -maxHeap[0]
        