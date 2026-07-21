class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []
        heapq.heapify(minHeap)

        for num in nums:
            heapq.heappush(minHeap, -num)
        
        for i in range(k):
            ans = heapq.heappop(minHeap)

        return -ans