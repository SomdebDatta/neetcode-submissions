class Solution:
    def reorganizeString(self, s: str) -> str:
        hashmap = defaultdict(int)

        for ch in s:
            hashmap[ch] += 1
        
        max_heap = [(-ct, ch) for ch, ct in hashmap.items()]

        prev = None
        res = ""

        while max_heap or prev:
            # There is no other char to append other than prev - return ""
            if prev and not max_heap:
                return ""

            cnt, ch = heapq.heappop(max_heap)
            res += ch
            cnt += 1

            if prev:
                heapq.heappush(max_heap, prev)
                prev = None
            
            if cnt != 0:
                prev = (cnt, ch)
        
        return res