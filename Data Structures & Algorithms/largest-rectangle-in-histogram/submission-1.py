class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        area = 0
        stack = [] # [idx, height]
        pop_idx = -1
        for idx, height in enumerate(heights):
            while stack and stack[-1][1] > height:
                pop_idx, pop_height = stack.pop()
                curr = (idx - pop_idx) * pop_height
                area = max(area, curr)
            if pop_idx > -1:
                stack.append([pop_idx, height])
                pop_idx = -1
            else:
                stack.append([idx, height])
        
        while stack:
            pop_idx, pop_height = stack.pop()
            curr = (len(heights) - pop_idx) * pop_height
            area = max(area, curr)
        
        return area