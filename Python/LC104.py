# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.dig(root)

    def dig(self, node):
        if node is None:
            return 0
        l = self.dig(node.left)
        r = self.dig(node.right)
        return max(l, r) + 1
    
#---------------------------
a = Solution()
t1 = TreeNode(3)
t1.left = TreeNode(9)
t1.right = TreeNode(20)
t1.right.left = TreeNode(15)
t1.right.right = TreeNode(7)
t1.right.right.left = TreeNode(4)

print a.maxDepth(t1)

