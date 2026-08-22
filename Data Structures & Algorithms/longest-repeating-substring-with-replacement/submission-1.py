class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap = defaultdict(int)
        l, r = 0, 0
        max_freq = 0
        ans = 0

        while r < len(s):
            hashmap[s[r]] += 1
            max_freq = max(max_freq, hashmap[s[r]])
            while (r - l + 1) - max_freq > k:
                
                hashmap[s[l]] -= 1
                l += 1
            ans = max(ans, (r - l + 1))
            r += 1
        
        return ans