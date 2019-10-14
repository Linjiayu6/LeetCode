# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

c# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root is not None:
            if val < root.val:
                # left tree
                if root.left is not None:
                    self.insertIntoBST(root.left, val)
                else:
                    root.left = TreeNode(val)
            else:
                # right tree
                if root.right is not None:
                    self.insertIntoBST(root.right, val)
                else:
                    root.right = TreeNode(val)
        return root

"""
Steps:
- root is not None:
- val < root.val: Left Tree  if root.left is not None: 迭代 else: root.left = treeNode(val)
- val >= root.val: Right Tree
"""