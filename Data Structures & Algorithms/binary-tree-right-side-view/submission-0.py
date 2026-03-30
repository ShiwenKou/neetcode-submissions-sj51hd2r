# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        from collections import deque

        dq = deque()
        if root:
            dq.append(root)

        res = []
        while dq:
            length = len(dq)
            rightNode = None
            for i in range(length):
                node = dq.popleft()
                rightNode = node.val
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            res.append(rightNode)
        return res

        