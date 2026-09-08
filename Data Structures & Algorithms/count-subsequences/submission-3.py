class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        curr = [0 for _ in range (len(t) + 1)]
        prev = [0 for _ in range (len(t) + 1)]
        curr[len(t)] = prev[len(t)] = 1

        for i in range(len(s) - 1, -1, -1):
            for j in range(len(t) - 1, -1, -1):
                curr[j] = prev[j]
                if s[i] == t[j]:
                    curr[j] += prev[j + 1]
            prev = curr[:]
        
        return curr[0]
