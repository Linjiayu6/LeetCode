# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

A, B, C, D = TreeNode(1), TreeNode(2), TreeNode(3), TreeNode(4)
A.left = B
A.right = C

B.left = D
