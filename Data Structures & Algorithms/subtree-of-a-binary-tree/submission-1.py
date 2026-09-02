# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def sameTree(p, q):
            if not p or not q:
                if not p and not q:
                    return True
                return False
            
            if p.val != q.val:
                return False
            
            return sameTree(p.left, q.left) and sameTree(p.right, q.right)
        
        subTree = False
        
        def dfs(node):
            nonlocal subTree
            if not node or subTree:
                return 
            
            if node.val == subRoot.val and sameTree(node, subRoot):
                subTree = True
            
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return subTree
            
            