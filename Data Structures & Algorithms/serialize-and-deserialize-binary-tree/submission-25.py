# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        def dfs(curr):
            if not curr:
                res.append('N')
                return
            res.append(str(curr.val))

            dfs(curr.left)
            dfs(curr.right)
        dfs(root)
        return '.'.join(res)



        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:

        lst = data.split('.')
        i = 0

        vals = iter(lst)
        def dfs():
            nonlocal i
            val = next(vals)
            if val == 'N':
                return None

            curr = TreeNode(val)

            curr.left = dfs()
            curr.right = dfs()
            
            return curr
        return dfs()
        
