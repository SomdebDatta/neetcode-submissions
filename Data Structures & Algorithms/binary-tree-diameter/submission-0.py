# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diam = 0

        def dfs(node):
            if not node:
                return 0
            
            leftHeight = 1 + dfs(node.left)
            rightHeight = 1 + dfs(node.right)

            self.diam = max(self.diam, leftHeight + rightHeight - 1)

            return max(leftHeight, rightHeight)
        
        dfs(root)
        return self.diam - 1