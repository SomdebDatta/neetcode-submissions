# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        ans = []

        def dfs(node):
            nonlocal ans

            if not node:
                ans.append('N')
                return
            
            ans.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        print(ans)
        return ','.join(ans)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        ip = data.split(',')
        idx = 0


        def dfs():
            nonlocal idx

            if idx >= len(ip):
                return
                
            if ip[idx] == 'N':
                return None
            
            node = TreeNode(ip[idx])
            idx += 1
            node.left = dfs()
            idx += 1
            node.right = dfs()

            return node
        return dfs()
