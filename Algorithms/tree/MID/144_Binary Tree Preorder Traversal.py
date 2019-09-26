
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
preorder: root -> left -> right
"""
class Solution(object):
    def __init__(self):
       self.L = []
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is not None:
            self.traverse(root)
        return self.L

    def traverse(self, node):
        if node is not None:
            # root -> left -> right
            self.L.append(node.val)
            self.traverse(node.left)
            self.traverse(node.right)
