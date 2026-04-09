# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        

        def same(p1, p2):
            if not p1 and not p2:
                return True
            
            if not p1 or not p2:
                return False
            
            if p1.val != p2.val:
                return False
            
            return same(p1.left, p2.left) and same(p1.right, p2.right)
        

        def dfs(root):
            if not root:
                return False
            
            if same(root, subRoot):
                return True
            
            return dfs(root.left) or dfs(root.right)

        
        return dfs(root)
