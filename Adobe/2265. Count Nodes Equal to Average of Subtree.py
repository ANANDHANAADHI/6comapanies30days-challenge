
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def dfs(node):
            if not node:
                return 0, 0
            
            ls, lc = dfs(node.left)
            rs, rc = dfs(node.right)
            tot = ls + rs + node.val
            cnt = lc + rc + 1
            if tot // cnt == node.val:
                self.ans += 1
            return tot, cnt
        
        dfs(root)
        return self.ans