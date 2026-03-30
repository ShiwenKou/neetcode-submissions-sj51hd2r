# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.dfs(root, root.val)

    def dfs(self, root, maxValue):

        if not root:
            return 0
        
        if root.val >= maxValue:
            res = 1
        else: res = 0
        maxValue = max(maxValue, root.val)
        res += self.dfs(root.left, maxValue)
        res += self.dfs(root.right, maxValue)

        return res

        