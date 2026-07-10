class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []

        def checkPali(start, end):
            if start == end:
                return True
            
            while start < end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True

        def dfs(curr, pos):
            if pos == len(s):
                ans.append(curr.copy())
                return
            
            for i in range(pos, len(s)):
                if checkPali(pos, i):
                    curr.append(s[pos: i + 1])
                    dfs(curr, i + 1)
                    curr.pop()
        
        dfs([], 0)
        return ans