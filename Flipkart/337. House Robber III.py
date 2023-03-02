def helper(root,d,flag):
    if root==None:
        return 0
    if flag==None:
        if d[root][0]!=None and d[root][1]!=None:
            return max(d[root])
    if flag==False:
        if d[root][0]!=None:
            return d[root][0]
    # Exclude 
    d[root][0] = helper(root.left,d,None)+helper(root.right,d,None)
    
    # Include
    d[root][1] = root.val + helper(root.left,d,False)+helper(root.right,d,False)
    
    if flag==None:
        return max(d[root])
    if flag==False:
        return d[root][0]
    
def dfs(root,d):
    if root==None:
        return
    dfs(root.left,d)
    d[root] = [None,None]
    dfs(root.right,d)
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        d = {}
        dfs(root,d)
        return helper(root,d,None)