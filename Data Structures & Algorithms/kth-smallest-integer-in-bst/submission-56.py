# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []
        n = 0
        def dfs(root):
            nonlocal n
            if not root:
                return
            


            dfs(root.left)
            n += 1
            if n == k:
                res.append(root.val)
            dfs(root.right)

        dfs(root)
        return res[0]

        