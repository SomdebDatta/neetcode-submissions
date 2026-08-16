class Solution:
    def trap(self, height: List[int]) -> int:
        lmax, rmax = 0, 0
        l, r = 0, len(height) - 1
        ans = 0

        while l < r:
            lmax = max(lmax, height[l])
            rmax = max(rmax, height[r])

            ans += lmax - height[l] + rmax - height[r]

            if lmax < rmax:
                l += 1
            else:
                r -= 1
        
        return ans