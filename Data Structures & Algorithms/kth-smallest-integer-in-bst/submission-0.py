# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(root, ls):
            if (root == None) or (len(ls) >= k):
                return
            dfs(root.left, ls)
            ls.append(root.val)
            dfs(root.right, ls)

        ans = []
        dfs(root, ans)

        return ans[k-1]