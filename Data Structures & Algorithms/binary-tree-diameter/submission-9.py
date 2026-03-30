# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.largest_diameter = 0
        self.height(root)
        return self.largest_diameter
        
    def height(self, root):
        if not root:
            return 0

        left_height = self.height(root.left)
        right_height = self.height(root.right)
        diameter = left_height + right_height
        self.largest_diameter = max(self.largest_diameter, diameter)

        return 1 + max(left_height, right_height)

        