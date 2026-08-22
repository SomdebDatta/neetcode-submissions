class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        area = 0
        stack = [] # [idx, height]
        pop_idx = -1
        for idx, height in enumerate(heights):
            pop_idx = idx
            while stack and stack[-1][1] > height:
                pop_idx, pop_height = stack.pop()
                curr = (idx - pop_idx) * pop_height
                area = max(area, curr)
            stack.append([pop_idx, height])
        
        while stack:
            pop_idx, pop_height = stack.pop()
            curr = (len(heights) - pop_idx) * pop_height
            area = max(area, curr)
        
        return area