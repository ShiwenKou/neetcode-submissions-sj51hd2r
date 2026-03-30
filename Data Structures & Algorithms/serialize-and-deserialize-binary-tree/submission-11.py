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
        self.dfsSerialize(root)
        return '.'.join(self.res)

    def dfsSerialize(self, root):
        if not root:
            self.res.append('N')
            return

        self.res.append(str(root.val))

        self.dfsSerialize(root.left)
        self.dfsSerialize(root.right)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        self.lst = data.split('.')
        self.i = 0
        return self.dfs()


    def dfs(self):
        if self.lst[self.i] == "N":
            self.i += 1
            return None

        root = TreeNode(int(self.lst[self.i]))
        self.i += 1
        root.left = self.dfs()
        root.right = self.dfs()

        return root
