class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        def checkPali(l, r):
            if l == r:
                return True
            
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        def dfs(idx, curr):
            if idx == len(s):
                ans.append(curr.copy())
                return
            
            for pos in range(idx, len(s)):
                if checkPali(idx, pos):
                    curr.append(s[idx: pos + 1])
                    dfs(pos + 1, curr)
                    curr.pop()
        
        dfs(0, [])
        return ans