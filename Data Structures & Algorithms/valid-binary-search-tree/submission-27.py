# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.flag = True
        self.dfs(root, float('-inf'), float('inf'))
        return self.flag

    def dfs(self, root, minn, maxx):
        if not root:
            return
    
        if not (root.val> minn and root.val < maxx):
            self.flag = False
        self.dfs(root.left, minn, root.val)
        self.dfs(root.right, root.val, maxx)
        