class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []

        for stone in stones:
            heapq.heappush(max_heap, -stone)
        
        if not max_heap:
            return 0
        
        while len(max_heap) > 1:
            stone1 = -heapq.heappop(max_heap)
            stone2 = -heapq.heappop(max_heap)

            if stone1 == stone2:
                continue
            
            heapq.heappush(max_heap, -(abs(stone1 - stone2)))
        
        if not max_heap:
            return 0
        
        return -heapq.heappop(max_heap)