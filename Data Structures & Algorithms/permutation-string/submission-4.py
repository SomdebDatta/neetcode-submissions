class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        s1_map = [0] * 26
        s2_map = [0] * 26

        for letter in s1:
            s1_map[ord(letter) - ord('a')] += 1
        
        l, r = 0, 0

        while r < len(s1): # Maintaining the window size
            s2_map[ord(s2[r]) - ord('a')] += 1
            r += 1

        while r < len(s2):
            if s2_map == s1_map:
                return True
            
            s2_map[ord(s2[l]) - ord('a')] -= 1
            l += 1
            
            s2_map[ord(s2[r]) - ord('a')] += 1  
            r += 1      

        return s2_map == s1_map
