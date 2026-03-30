# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxDiameter = 0
        self.dfs(root)
        return self.maxDiameter

    def dfs(self, root):

        if not root:
            return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        diameter = left + right
        self.maxDiameter = max(self.maxDiameter, diameter)

        return 1 + max(left, right)
        