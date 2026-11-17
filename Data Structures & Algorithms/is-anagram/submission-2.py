class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hash = [0] * 26
        t_hash = [0] * 26

        if len(s) != len(t):
            return False
        
        for s_char, t_char in zip(s, t):
            s_hash[ord(s_char) - 96 - 1] += 1
            t_hash[ord(t_char) - 96 - 1] += 1
        
        return s_hash == t_hash