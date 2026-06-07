# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ret = []
        if not root:
            return ret
        
        ret = [root.val]
        def dfs(now: TreeNode, depth: int):
            if not now:
                return
            if depth == len(ret):
                ret.append(now.val)
            
            dfs(now.right, depth + 1)
            dfs(now.left, depth + 1)
            

        dfs(root, 0)
        return ret
        