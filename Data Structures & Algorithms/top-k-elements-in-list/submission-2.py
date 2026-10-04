class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hashmap = Counter(nums)
        min_heap = []

        # for num in nums:
        #     hashmap[num] += 1
        
        for num, ct in hashmap.items():
            heapq.heappush(min_heap, (-ct, num))
        
        ans = []
        
        for _ in range(k):
            ct, num = heapq.heappop(min_heap)
            ans.append(num)
        
        return ans