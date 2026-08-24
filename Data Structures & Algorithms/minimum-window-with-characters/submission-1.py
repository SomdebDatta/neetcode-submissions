class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        res = ""
        lenRes = float("infinity")

        t_map = defaultdict(int)
        s_map = defaultdict(int)

        for letter in t:
            t_map[letter] += 1
        
        have, need = 0, len(t_map)
        l, r = 0, 0

        while r < len(s):
            s_map[s[r]] += 1
            if s_map[s[r]] == t_map[s[r]]:
                have += 1
            while have == need:
                if (r - l + 1) < lenRes:
                    res = s[l: r + 1]
                    lenRes = r - l + 1
                s_map[s[l]] -= 1
                if s_map[s[l]] < t_map[s[l]]:
                    have -= 1
                l += 1
            
            r += 1
        
        return res