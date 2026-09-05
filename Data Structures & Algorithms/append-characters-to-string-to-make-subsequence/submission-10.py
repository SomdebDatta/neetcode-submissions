class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        max_common = 0

        
        def check_common2(idx):
            t_idx, s_idx = 0, idx
            ct = 0
            while s_idx < len(s) and t_idx < len(t):
                if s[s_idx] == t[t_idx]:
                    ct += 1
                    t_idx += 1
                s_idx += 1
            return ct

        for i in range(min(len(s), len(t))):
            if s[i] == t[0]:
                max_common = max(max_common, check_common2(i))
        
        return len(t) - max_common