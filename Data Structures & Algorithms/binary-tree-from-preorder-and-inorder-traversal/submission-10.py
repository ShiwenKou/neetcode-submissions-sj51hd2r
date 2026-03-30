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
        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])

        # left: we want preorder[1: 1+mid], inorder[:mid]
        # right : we want preorder[mid+1: ], inorder[mid+1:]
        root.left = self.buildTree(preorder[1: 1 + mid], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])
        
        return root