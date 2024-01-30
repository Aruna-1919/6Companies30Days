# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        t = 0
        def dfs(root):
            if not root.left and not root.right:
                return [1]
            nonlocal t
            l_d = dfs(root.left) if root.left else []
            r_d = dfs(root.right) if root.right else []

            for i in l_d:
                if i >= distance: 
                    continue
                for k in r_d:
                    if i + k <= distance:
                        t += 1
            
            return [i+1 for i in l_d+r_d]
        

        dfs(root)
        return t
