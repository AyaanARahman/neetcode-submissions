class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        arr = []  # Stores values in sorted order
        
        def dfs(node):
            if not node:
                return

            # Inorder: left → root → right
            #automatically sorts it since it's in ascending order
            dfs(node.left)
            arr.append(node.val)
            dfs(node.right)

        dfs(root)

        #zero-indexed k=3 arr[3-1] = arr[2] (3rd smallest number)
        return arr[k - 1]