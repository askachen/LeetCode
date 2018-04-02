# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """        
        return self.merge(t1, t2)

    def merge(self, n1, n2):
        if n1 is None and n2 is None:
            return None
        if n1 is None:
            return n2
        if n2 is None:
            return n1
        n = TreeNode(n1.val + n2.val)
        n.left = self.merge(n1.left, n2.left)
        n.right = self.merge(n1.right, n2.right)
        return n
    
#---------------------------
    
a = Solution()
t1 = TreeNode(1)
t1.left = TreeNode(3)
t1.left.left = TreeNode(5)
t1.right = TreeNode(2)

t2 = TreeNode(2)
t2.left = TreeNode(1)
t2.left.right = TreeNode(4)
t2.right = TreeNode(3)
t2.right.right = TreeNode(7)

print a.mergeTrees(t1, t2)


