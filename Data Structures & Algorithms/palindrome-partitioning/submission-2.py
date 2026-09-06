class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        
        def check_palindrome(word):
            l, r = 0, len(word) - 1

            while l < r:
                if word[l] != word[r]:
                    return False
                l += 1
                r -= 1
            
            return True

        def backtracking(idx, curr):
            if idx >= len(s):
                ans.append(curr.copy())
                return
            
            for i in range(idx, len(s)):
                temp = s[idx: i + 1]
                if temp and check_palindrome(temp):
                    curr.append(temp)
                    # print(temp)
                    backtracking(i + 1, curr)
                    curr.pop()
        
        backtracking(0, [])

        return ans