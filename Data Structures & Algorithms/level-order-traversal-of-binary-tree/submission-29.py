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
            length = len(dq)
            sol = []
            for _ in range(length):
                cur = dq.popleft()
                sol.append(cur.val)

                if cur.left:
                    dq.append(cur.left)
                if cur.right:
                    dq.append(cur.right)
            res.append(sol)
        return res

