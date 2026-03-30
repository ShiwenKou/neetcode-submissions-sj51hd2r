# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0
        self.height(root)
        return self.max_diameter
    
    def height(self, root):

        if not root:
            return 0

        left = self.height(root.left)
        right = self.height(root.right)


        diameter = left + right
        self.max_diameter = max(self.max_diameter, diameter)

        return 1 + max(left, right)
        