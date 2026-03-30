# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        total = 0
        def dfs(root, maxx):
            nonlocal total
            if not root:
                return 0

            if root.val >= maxx:
                total += 1
            maxx = max(root.val, maxx)
            dfs(root.left, maxx)
            dfs(root.right, maxx)

            return total
        return dfs(root, root.val)
        