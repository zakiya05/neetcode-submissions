class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = float('-inf')

        def dfs(node):
            if not node:
                return 0

            # ignore negative paths
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)

            # best path THROUGH this node
            self.ans = max(self.ans, node.val + left + right)

            # return best one-side path upward
            return node.val + max(left, right)

        dfs(root)
        return self.ans