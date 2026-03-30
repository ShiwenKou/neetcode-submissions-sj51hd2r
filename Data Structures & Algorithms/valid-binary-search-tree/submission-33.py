# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return False

        def validate(root, minn, maxx):
            if not root:
                return True
            
            if not (minn < root.val < maxx):
                return False
            
            return validate(root.left, minn, root.val) and validate(root.right, root.val, maxx)
        
        return validate(root, float('-inf'), float('inf'))