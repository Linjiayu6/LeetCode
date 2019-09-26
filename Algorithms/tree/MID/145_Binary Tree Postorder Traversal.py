# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.L = []
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is not None:
            self.traverse(root)
        return self.L

    def traverse(self, node):
        if node is not None:
            # left -> right -> root
            self.traverse(node.left)
            self.traverse(node.right)
            self.L.append(node.val)