class Solution:
    def trap(self, height: List[int]) -> int:
        # l, r, lmax, rmax = 0, 0, 0, 0
        l = lmax = rmax = 0
        r = len(height) - 1
        total = 0

        while l < r:
            lmax = max(height[l], lmax)
            rmax = max(height[r], rmax)

            if lmax < rmax:
                total += lmax - height[l]
                l += 1
            else:
                total += rmax - height[r]
                r -= 1
        
        return total