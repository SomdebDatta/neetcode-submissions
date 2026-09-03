# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        ans = float('-inf')

        def dfs(node):
            nonlocal ans

            if not node:
                return 0
            
            leftval = max(dfs(node.left), 0)
            rightval = max(dfs(node.right), 0)

            ans = max(ans, leftval + rightval + node.val)

            return node.val + max(leftval, rightval)

        dfs(root)

        return ans