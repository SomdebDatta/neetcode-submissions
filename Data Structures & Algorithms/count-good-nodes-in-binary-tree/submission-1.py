# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = []

        def dfs(curr, maxi):
            if not curr:
                return
            
            maxi = max(maxi, curr.val)
            if maxi <= curr.val:
                ans.append(curr.val)
            dfs(curr.left, maxi)
            dfs(curr.right, maxi)
            
        dfs(root, float('-inf'))
        return len(ans)