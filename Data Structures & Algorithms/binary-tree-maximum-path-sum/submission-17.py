# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        maxDiameter = float('-inf')
        def dfs(root):
            nonlocal maxDiameter
            if not root:
                return 0

            left = max(dfs(root.left), 0)
            right = max(dfs(root.right), 0)

            diameter = root.val + left + right
            maxDiameter = max(maxDiameter, diameter)

            return root.val + max(left, right)
        dfs(root)
        return maxDiameter