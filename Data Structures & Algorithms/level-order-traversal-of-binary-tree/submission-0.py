from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        if root is None:
            return []

        queue = deque([root])
        while len(queue) > 0:
            # kinda like freezing the tree and processessing whatever's on that layer
            curr_size = len(queue)
            new_level = []
            # for each thing in this level
            for _ in range(curr_size):
                node = queue.popleft()
                new_level.append(node.val)
                for child in [node.left, node.right]:
                    if child is not None:
                        queue.append(child)
            res.append(new_level)
        return res
        


        