# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        self.res = []
        self.dfs_serialize(root)
        return ','.join(self.res)
    def dfs_serialize(self, root):
        if not root:
            self.res.append('N')
            return
        self.res.append(str(root.val))
        self.dfs_serialize(root.left)
        self.dfs_serialize(root.right)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        self.data = data.split(',')
        self.i = 0
        return self.dfs_deserialize()
        
    def dfs_deserialize(self):

        if self.data[self.i] == 'N':
            self.i += 1
            return None

        
        node = TreeNode(int(self.data[self.i]))
        self.i += 1
        node.left = self.dfs_deserialize()
        node.right = self.dfs_deserialize()
        return node

