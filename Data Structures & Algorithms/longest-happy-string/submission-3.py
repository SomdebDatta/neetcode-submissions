class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        min_heap = []

        if a:
            heapq.heappush(min_heap, (-a, 'a'))
        if b:
            heapq.heappush(min_heap, (-b, 'b'))
        if c:
            heapq.heappush(min_heap, (-c, 'c'))


        ans = ''

        while min_heap:
            cnt, curr = heapq.heappop(min_heap)
            if len(ans) > 1 and curr == ans[-1] == ans[-2]:
                if not min_heap:
                    break
                cnt2, curr2 = heapq.heappop(min_heap)
                ans += curr2
                cnt2 += 1
                if cnt2:
                    heapq.heappush(min_heap, (cnt2, curr2))

            ans += curr
            cnt += 1
            if cnt:
                heapq.heappush(min_heap, (cnt, curr))
        
        return ans