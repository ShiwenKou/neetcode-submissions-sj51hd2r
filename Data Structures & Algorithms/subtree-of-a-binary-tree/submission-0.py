# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        return self.has_subtree(root, subRoot)
    
    def has_subtree(self, root, subRoot):
        if not root:
            return False
        
        if self.same(root, subRoot):
            return True

        return self.has_subtree(root.left, subRoot) or self.has_subtree(root.right, subRoot)

    def same(self, p, q):

        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        
        return self.same(p.left, q.left) and self.same(p.right, q.right)
        