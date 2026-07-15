# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        inorder = []

        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            inorder.append(node)
            dfs(node.right)
        
        dfs(root)
        first_idx = -1
        for idx in range(len(inorder) - 1):
            if first_idx == -1 and inorder[idx].val > inorder[idx + 1].val:
                first_idx = idx
                swap_idx = idx + 1
                continue
            if inorder[idx].val > inorder[idx + 1].val:
                swap_idx = idx + 1
        
        inorder[first_idx].val, inorder[swap_idx].val = inorder[swap_idx].val, inorder[first_idx].val
        
        return
