# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        '''
        curr = root
        while (curr != None):
            if ((p.val < curr.val) and (q.val < curr.val)):
                curr = curr.left
            elif ((p.val > curr.val) and (q.val > curr.val)):
                curr = curr.right
            else:
                return curr

        return None
        '''
        if not root:
            return None
        if root.val == p.val or root.val == q.val:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        if left:
            return left

        return right
        