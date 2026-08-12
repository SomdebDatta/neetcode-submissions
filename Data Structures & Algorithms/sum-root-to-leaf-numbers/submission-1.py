# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        q = deque([(root, 0)])
        total = 0

        while q:
            for _ in range(len(q)):
                node, curr_sum = q.popleft()
                curr_sum = curr_sum * 10 + node.val

                if not node.right and not node.left:
                    total += curr_sum
                    continue
                
                if node.left:
                    q.append((node.left, curr_sum))
                if node.right:
                    q.append((node.right, curr_sum))
        return total