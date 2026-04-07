# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check_node(node, left, right):
            if node == None:
                return True
                
            if (node.val <= left) or (node.val >= right):
                return False

            return (
                check_node(node.left, left, node.val) and
                check_node(node.right, node.val, right)
            )
        
        return check_node(root, -float("inf"), float("inf"))