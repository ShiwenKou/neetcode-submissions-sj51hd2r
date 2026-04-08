# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        


        def dfs(root, minn, maxx):

            if not root:
                return True
            if not(minn < root.val < maxx):
                return False
            return dfs(root.left, minn, root.val) and dfs(root.right, root.val, maxx)
        
        return dfs(root, float('-inf'), float('inf'))
