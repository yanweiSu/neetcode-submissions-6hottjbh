# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ret = []
        if not root:
            return ret

        queue = deque([root])
        layer_size = 1
        while (queue):
            layer_ret = []
            next_layer_size = 0
            for _ in range(layer_size):
                curr = queue.popleft()
                layer_ret.append(curr.val)
                if curr.left:
                    queue.append(curr.left)
                    next_layer_size += 1
                if curr.right:
                    queue.append(curr.right)
                    next_layer_size += 1
            
            layer_size = next_layer_size
            ret.append(layer_ret)

        return ret


            