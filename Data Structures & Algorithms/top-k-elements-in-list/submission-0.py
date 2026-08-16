class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        max_heap = [] #(-ct, num)

        num_ct = defaultdict(int)

        for num in nums:
            num_ct[num] += 1
        
        for num, ct in num_ct.items():
            heapq.heappush(max_heap, (-ct, num))
        
        ans = []

        for i in range(k):
            _, num = heapq.heappop(max_heap)
            ans.append(num)
        
        return ans