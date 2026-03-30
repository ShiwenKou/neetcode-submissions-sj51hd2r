# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.dfs(root, root.val)
    def dfs(self, root, maxx):

        if not root:
            return 0

        if root.val >= maxx:
            res = 1
        else:
            res = 0
        maxx = max(maxx, root.val)
        res += self.dfs(root.left, maxx)
        res += self.dfs(root.right, maxx)

        return res