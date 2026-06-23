# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        stack = deque([root])
        ans = []

        while stack:
            curr = []
            for _ in range(len(stack)):
                node = stack.popleft()
                curr.append(node.val)
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            if curr:
                ans.append(curr)
        
        return ans