class Solution:
    def longestPalindrome(self, s: str) -> str:
        cache = [[False for _ in range(len(s) + 1)] for _ in range(len(s) + 1)]
        ansidx, anslen = 0, 0

        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j] and (j - i <= 2 or cache[i + 1][j - 1]):
                    cache[i][j] = True
                    if (j - i + 1) > anslen:
                        ansidx = i
                        anslen = j - i + 1
        
        return s[ansidx: ansidx + anslen]