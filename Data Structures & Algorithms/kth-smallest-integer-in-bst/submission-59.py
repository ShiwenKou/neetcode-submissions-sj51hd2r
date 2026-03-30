# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        res = root.val
        curr = root
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            
            curr = stack.pop()

            k -= 1
            if k == 0:
                res = curr.val
                break
            curr = curr.right
        return res
# each node visited once, O(n)
# space, we maintained a stack, at most contain n nodes, so O(n)