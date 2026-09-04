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
        bst_sorted = []

        def dfs(node):
            if not node:
                return
            
            dfs(node.left)
            print(node.val)
            bst_sorted.append(node)
            dfs(node.right)
        
        dfs(root)
        print(bst_sorted)
        first, second = None, None

        for i in range(len(bst_sorted) - 1):
            if bst_sorted[i].val > bst_sorted[i + 1].val:
                second = i + 1
                if first is None:
                    first = i
                else:
                    break
        
        # first.val, second.val = second.val, first.val
        


        
        bst_sorted[first].val, bst_sorted[second].val = bst_sorted[second].val, bst_sorted[first].val

        
