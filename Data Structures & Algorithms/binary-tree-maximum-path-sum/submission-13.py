# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        self.maxPath = float('-inf')
        self.dfs(root)
        return self.maxPath
    
    def dfs(self, root):

        if not root:
            return 0

        left = max(self.dfs(root.left), 0)
        right = max(self.dfs(root.right), 0)

        path = root.val + left + right
        self.maxPath = max(self.maxPath, path)
        
        return root.val + max(left, right)
        