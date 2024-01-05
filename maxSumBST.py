class Solution(object):
    def maxSumBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        result = [float('-inf')] 
        
        def BST(root):
            if root == None:
                return [float('inf'), float('-inf'), 0]
            
            left = BST(root.left)
            right = BST(root.right)
            
            if left[1] >= root.val or right[0] <= root.val:
                return [float('-inf'), float('inf'), 0]
            
            subtree_sum = left[2] + root.val + right[2]
            result[0] = max(result[0], subtree_sum) 
            
            return [min(root.val, left[0]), 
                    max(root.val, right[1]),
                    subtree_sum]
        
        BST(root)
        
        return max(result[0], 0)
