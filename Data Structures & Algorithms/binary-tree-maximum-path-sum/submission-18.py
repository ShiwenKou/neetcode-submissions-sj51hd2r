# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        

        maxRes = float('-inf')
        def dfs(root):
            nonlocal maxRes
            if not root:
                return 0

            left = max(dfs(root.left), 0)
            right = max(dfs(root.right), 0)

            maxRes = max(root.val + left + right, maxRes) # track no spliting res
            return root.val + max(left, right) # pass back with splitted res

        dfs(root)
        return maxRes