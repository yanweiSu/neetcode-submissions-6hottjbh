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

        val2inorder_index = {inorder[i]: i for i in range(len(inorder))}

        def helper(pre_left, pre_right, in_left, in_right) -> TreeNode:
            if (pre_right < pre_left) or (in_right < in_left):
                return None

            root = TreeNode()
            root.val = preorder[pre_left]
            root_idx = val2inorder_index[root.val]

            left_size = root_idx - in_left
            right_size = in_right - root_idx

            root.left = helper(pre_left + 1, pre_left + left_size, in_left, in_left + left_size - 1)
            root.right = helper(pre_right - right_size + 1, pre_right, in_right - right_size + 1, in_right)

            return root

        return helper(0, len(preorder) - 1, 0, len(preorder) - 1)

