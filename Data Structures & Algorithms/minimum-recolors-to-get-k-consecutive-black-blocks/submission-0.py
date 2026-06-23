class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l, change, ans = 0, 0, 101

        for r in range(len(blocks)):
            if blocks[r] == 'W':
                change += 1
            while (r - l + 1) > k:
                if blocks[l] == 'W':
                    change -= 1
                l += 1
            if (r - l + 1) == k:
                ans = min(ans, change)
        return ans
            