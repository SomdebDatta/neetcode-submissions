# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        

        def dfs(node):
            if not node:
                return [0, 0] # with node, without node
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            max_with_node = node.val + left[1] + right[1]
            max_without_node = max(left) + max(right)
            return [max_with_node, max_without_node]
        
        return max(dfs(root))