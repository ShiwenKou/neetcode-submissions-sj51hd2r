# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        if not preorder:
            return None
        node = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        # left part. preorder we want 1-1+mid,  for inorder we want 0-mid(no mid)
        # right part, preorder we want mid+1 - end, for inorder we want mid+ 1 to the end

        node.left = self.buildTree(preorder[1: mid + 1], inorder[:mid])
        node.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return node
        