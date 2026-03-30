# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.res = []
        self.dfs(root, 0)
        return self.res


    def dfs(self, root, depth):
        if not root:
            return
        
        if depth == len(self.res):
            self.res.append(root.val)

        self.dfs(root.right, depth + 1)
        self.dfs(root.left, depth + 1)
        