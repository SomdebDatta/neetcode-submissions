class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        last, secondLast = 1, 1
        ans = 0

        for _ in range(n - 2, -1, -1):
            ans = last + secondLast
            secondLast = last
            last = ans
        
        return ans