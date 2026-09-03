# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = []

        def dfs(node, maxi):
            nonlocal ans

            if not node:
                return
            
            if node.val >= maxi:
                ans.append(node.val)
                maxi = node.val
            dfs(node.left, maxi)
            dfs(node.right, maxi)
        
        dfs(root, -101)
        return len(ans)