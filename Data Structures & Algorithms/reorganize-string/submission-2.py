class Solution:
    def reorganizeString(self, s: str) -> str:
        char_ct = defaultdict(int)

        for ch in s:
            char_ct[ch] += 1
        
        max_heap = []
        print(char_ct)
        for ch, ct in char_ct.items():
            if ct > (len(s) + 1) // 2:
                return ""
            heapq.heappush(max_heap, (-ct, ch))
        
        ans = ''

        while max_heap:
            ct, next_char = heapq.heappop(max_heap)
            if not ans or ans[-1] != next_char:
                ans += next_char
                if ct != -1:
                    heapq.heappush(max_heap, (ct + 1, next_char))
            else:
                next_next_ct, next_next_char = heapq.heappop(max_heap)
                ans += next_next_char
                if next_next_ct != -1:
                    heapq.heappush(max_heap, (next_next_ct + 1, next_next_char))
                heapq.heappush(max_heap, (ct, next_char))
        return ans