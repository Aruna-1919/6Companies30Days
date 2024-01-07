class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        root = Node(1)
        temp = root
        for i in range(2, n + 1):
            new_node = Node(i)
            temp.right = new_node
            new_node.left = temp
            temp = new_node
        temp.right = root
        root.left = temp

        while root.right != root:
            for i in range(k - 1):
                root = root.right
            root.left.right = root.right
            root.right.left = root.left
            root = root.right  

        return root.val

