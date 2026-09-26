# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ct = 0
        

        def recursion(node, curr_max):
            nonlocal ct
            if not node:
                return
            
            if node.val >= curr_max:
                ct += 1
            
            curr_max = max(curr_max, node.val)

            recursion(node.left, curr_max)
            recursion(node.right, curr_max)
        
        recursion(root, float('-inf'))

        return ct