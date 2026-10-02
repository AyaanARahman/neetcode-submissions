# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True
        
        def dfs(node, lowerBound, higherBound):
            if not node:
                return True

            #ensures that each child is kept within a certain bound
            if not (node.val > lowerBound and node.val < higherBound):
                return False
            
            leftSubtree = dfs(node.left, lowerBound, node.val)
            rightSubtree = dfs(node.right, node.val, higherBound)

            return (leftSubtree and rightSubtree)
        
        return dfs(root, float('-inf'), float('inf'))

        
        