class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_heap = [] # [num, index]
        l, r = 0, 0
        ans = []

        while (r - l + 1) <= k:
            heapq.heappush(max_heap, [-nums[r], r])
            r += 1
        ans.append(-max_heap[0][0])
        l += 1


        while r < len(nums):

            while max_heap and max_heap[0][1] not in range(l, r + 1):
                print('popping')
                heapq.heappop(max_heap)
            
            heapq.heappush(max_heap, [-nums[r], r])    
            ans.append(-max_heap[0][0])
            
            r += 1
            l += 1
        
        return ans