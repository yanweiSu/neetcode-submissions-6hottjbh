# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def countGoodNodes(now, x):
            if not now:
                return 0

            count = 0
            if now.val >= x:
                count += 1
            count += countGoodNodes(now.left, max(x, now.val))
            count += countGoodNodes(now.right, max(x, now.val))

            return count

        return countGoodNodes(root, -float('inf'))

        

