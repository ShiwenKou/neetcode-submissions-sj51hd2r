# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxSum = float('-inf')
        self.dsf(root)
        return self.maxSum

    def dsf(self, root):

        if not root:
            return 0

        left = max(self.dsf(root.left), 0)
        right = max(self.dsf(root.right), 0 )

        self.maxSum = max(self.maxSum, left + right + root.val)

        return root.val + max(left, right)

        