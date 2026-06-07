# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not (preorder and inorder):
            return None

        # Find root's index in inorder
        root_idx = 0
        while (inorder[root_idx] != preorder[0]):
            root_idx += 1

        inorder_left = []
        preorder_left = []
        inorder_right = []
        preorder_right = []

        if root_idx > 0:
            inorder_left = inorder[:root_idx]
            preorder_left = preorder[1:1 + root_idx]
        if root_idx < len(inorder) - 1:
            inorder_right = inorder[root_idx + 1:]
            preorder_right = preorder[1 + root_idx:]

        root = TreeNode()
        root.val = preorder[0]
        root.left = self.buildTree(preorder_left, inorder_left)
        root.right = self.buildTree(preorder_right, inorder_right)

        return root

