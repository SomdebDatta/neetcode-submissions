# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        vals = []

        def preorder(node):
            if not node:
                return
            
            preorder(node.left)
            vals.append(node.val)
            preorder(node.right)
        preorder(root)

        for i in range(len(vals) - 1):
            if vals[i] >= vals[i + 1]:
                return False
        return True