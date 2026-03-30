# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        dq = collections.deque()
        dq.append(root)
        res = []
        while dq:
            level = []
            length = len(dq)
            for _ in range(length):
                curr = dq.popleft()
                level.append(curr.val)
                if curr.left:
                    dq.append(curr.left)
                if curr.right:
                    dq.append(curr.right)
            res.append(level)
        return res